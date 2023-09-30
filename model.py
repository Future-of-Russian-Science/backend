from inference.face_inference import FaceInference, Models, Response
from message import Error, Success
from copy import deepcopy

infer = FaceInference(device='cpu', model=Models.mobilenet_v3_large_facial)


def get_response(path: str, _id: int):
    response = infer.predict(path)

    match response:
        case Response.real:
            res = deepcopy(Success.LiveFace)
            res['id'] = _id
            return res

        case Response.spoof:
            res = deepcopy(Error.FakeFace)
            res['id'] = _id
            return res

        case Response.no_face:
            res = deepcopy(Error.NoFace)
            res['id'] = _id
            return res
