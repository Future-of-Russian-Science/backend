from facenet_pytorch.models.mtcnn import MTCNN
import cv2


class FaceDetector:
    def __init__(self, device=None):
        self.device = device
        if self.device is None:
            self.device = 'cpu'

        self.mtcnn = MTCNN(image_size=224, margin=20, keep_all=True, device=device, min_face_size=100,
                           thresholds=[0.95, 0.95, 0.95])

    def load_image(self, filepath):
        # Load image
        frame = cv2.imread(filepath)

        # Convert to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        return frame

    def get_face(self, frame):
        # Detect faces
        try:
            boxes, probs, points = self.mtcnn.detect(frame, landmarks=True)
        except:
            return None

        faces = self.mtcnn.extract(frame, boxes, save_path='face.jpg')

        if faces is None:
            return None

        all_faces = len(faces)

        # get bigger face and crop it
        face = (faces[0], 1)
        for i in range(len(faces)):
            if faces[i].shape[0] > face[0].shape[0]:
                face = (faces[i], i + 1)

        return all_faces, face[1]
