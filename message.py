class Error():
    FileNotUploaded = {
        "Status": "Failed",
        "Message": "File not uploaded"
    }
    NotAllowedFormat = {
        "Status": "Failed",
        "Message": "This file format not allowed"
    }
    IncorrectParameter = {
        "Status": "Failed",
        "Message": "Incorrect request parameter"
    }
    FakeFace = {
        "Status": "Failed",
        "Message": "Fake face on picture"
    }
    NoFace = {
        "Status": "Failed",
        "Message": "No face found in the photo"
    }

class Success():
    LiveFace = {
        "Status": "ok",
        "Message": "Success, live face"
    }
