from message import Error, Success
from copy import deepcopy
import random
def mock(path, id):
    x = random.randint(1,3)

    match x:
        case 1:
            res = deepcopy(Error.NoFace)
            res['id'] = id
            return res
        case 2:
            res = deepcopy(Error.FakeFace)
            res['id'] = id
            return res
        case 3:
            res = deepcopy(Success.LiveFace)
            res['id'] = id
            return res
