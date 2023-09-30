from inference.face_detect import FaceDetector
from inference.face_spoof import SpoofDetector, Models
import torch
from enum import Enum
import cv2


class Response(str, Enum):
    real = "real"
    spoof = "spoof"
    no_face = "no_face"


class FaceInference:
    def __init__(self, device, model: Models):
        self.device = device
        self.face_detector = FaceDetector(device=device)
        self.spoof_detector = SpoofDetector(device=device, model=model)

    def predict(self, filepath):
        frame = self.face_detector.load_image(filepath)
        face = self.face_detector.get_face(frame)

        if face is None:
            return Response.no_face

        faces_count, face_idx = face

        if face_idx == 1:
            filename = 'face.jpg'
        else:
            filename = f'face_{face_idx}.jpg'

        print(filename)

        face = cv2.imread(filename)
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        prediction = self.spoof_detector.predict(face)

        # argmax
        prediction = torch.argmax(prediction, dim=1)

        if prediction == 0:
            return Response.real
        else:
            return Response.spoof
