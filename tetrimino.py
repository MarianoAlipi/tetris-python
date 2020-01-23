from enum import Enum

class Tetrimino:

    # Type of tetrimino
    class Type(Enum):
        I = 'I'
        O = 'O'
        T = 'T'
        J = 'J'
        L = 'L'
        S = 'S'
        Z = 'Z'

    # Paths to image for every type
    class Img(Enum):
        I = None
        O = None
        T = None
        J = None
        L = None
        S = None
        Z = None

    def __init__(self):
        self._type = None
        self._img = None
        self._rotation = 0
        # The position of the anchor block (independent of rotation)
        # Check which is the anchor block for every type
        self._anchor_pos = {'x': -1, 'y': -1}

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value

    @property
    def anchor_pos(self):
        return self._anchor_pos

    @anchor_pos.setter
    def anchor_pos(self, x, y):
        self._anchor_pos['x'] = x
        self._anchor_pos['y'] = y