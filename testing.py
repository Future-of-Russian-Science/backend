import csv
from os import listdir
from pathlib import PurePath
from inference.face_inference import FaceInference, Models, Response

infer = FaceInference(device='cpu', model=Models.mobilenet_v3_large_facial)

path = PurePath(__file__).parent


def test():
    files = listdir(str(path.joinpath('test_pic')))

    with open("output.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["filename", "preds"])

        for item in files:
            response = infer.predict(str(path.joinpath('test_pic').joinpath(item)))
            match response:
                case Response.real:
                    file_writer.writerow((item, 'real'))

                case Response.spoof:
                    file_writer.writerow((item, 'fake'))

                case Response.no_face:
                    file_writer.writerow((item, 'empty'))

test()
