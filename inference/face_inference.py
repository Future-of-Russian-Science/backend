from inference.face_detect import FaceDetector
from inference.face_spoof import SpoofDetector, Models
import torch
from enum import Enum


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

        prediction = self.spoof_detector.predict(face)

        # argmax
        prediction = torch.argmax(prediction, dim=1)

        if prediction == 0:
            return Response.real
        else:
            return Response.spoof
