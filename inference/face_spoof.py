import torch
from torchvision import models, transforms
from enum import Enum
from pathlib import Path


class Models(str, Enum):
    mobilenet_v3_large_facial_1 = "mobile_spoof_net_v3_1.pt"
    mobilenet_v3_large_facial_2 = "mobile_spoof_net_v3_1_2.pt"


class MobileSpoofNet(torch.nn.Module):
    def __init__(self, num_classes=2):
        super(MobileSpoofNet, self).__init__()
        self.model = models.mobilenet_v3_large(pretrained=True)
        self.model.classifier[-1] = torch.nn.Linear(1280, num_classes)

        # add regularization
        self.model.classifier.add_module("2", torch.nn.Dropout(p=0.15))
        self.model.classifier.add_module("3", torch.nn.ReLU())
        self.model.classifier.add_module("4", torch.nn.Linear(1280, 512))
        self.model.classifier.add_module("5", torch.nn.Dropout(p=0.15))
        self.model.classifier.add_module("6", torch.nn.ReLU())
        self.model.classifier.add_module("7", torch.nn.Linear(512, num_classes))

    def forward(self, x):
        x = self.model(x)
        return x


class SpoofDetector:
    def __init__(self, device, model: Models) -> None:
        self.device = device

        if self.device is None:
            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        # path to current dir
        self.basement = Path(__file__).parent.parent.absolute() / 'new_model'
        self.model_path = self.basement / model.value

        self.model = MobileSpoofNet()
        self.model.load_state_dict(torch.load(self.model_path, map_location=self.device))
        self.model = self.model.to(self.device)

    def transform(self, frame):
        transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

        return transform(frame)

    def predict(self, frame):
        frame = self.transform(frame)
        frame = frame.unsqueeze(0)
        frame = frame.to(self.device)

        self.model.eval()

        with torch.no_grad():
            logits = self.model(frame).cpu()
            print(logits)

        prediction = torch.softmax(logits, dim=1)
        print(prediction)

        return prediction

