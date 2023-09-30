from message import Error, Success
import random
def mock(image):
    x = random.randint(1,3)

    match x:
        case 1:
            return Error.NoFace
        case 2:
            return Error.FakeFace
        case 3:
            return Success.LiveFace
