from facenet_pytorch.models.mtcnn import MTCNN
import cv2


class FaceDetector:
    def __init__(self, device=None):
        self.device = device
        if self.device is None:
            self.device = 'cpu'

        self.mtcnn = MTCNN(image_size=224, margin=40, keep_all=True, device=device, min_face_size=100)

    def load_image(self, filepath):
        # Load image
        frame = cv2.imread(filepath)

        # Convert to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # flip
        frame = cv2.flip(frame, 1)

        return frame

    def get_face(self, frame):
        # Detect faces
        boxes, probs, points = self.mtcnn.detect(frame, landmarks=True)

        faces = self.mtcnn.extract(frame, boxes, save_path=None)

        if faces is None:
            return None

        # get bigger face and crop it
        face = faces[0]
        for i in range(len(faces)):
            if faces[i].shape[0] > face.shape[0]:
                face = faces[i]

        return face

