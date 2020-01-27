from enum import Enum

class Tetrimino:

    # The I Tetrimino occupies columns 4, 5, 6 and 7, the O Tetrimino occupies columns 5 and 6, and the remaining 5 Tetriminos occupy columns 4, 5 and 6.

    # Type of tetrimino
    class Type(Enum):
        I = 'I'
        O = 'O'
        T = 'T'
        J = 'J'
        L = 'L'
        S = 'S'
        Z = 'Z'

    def __init__(self, type=None, x=-1, y=-1):
        self._type = type
        self.img = "assets/tetriminos/" + type.value + ".png"
        # Which block is the anchor block (respect to the tetrimino's image).
        # Starts at 0.
        anchorBlockX, anchorBlockY, self._rotation = self._determineAnchorBlockAndRotation(type)
        self._anchor_block = {'x': anchorBlockX, 'y': anchorBlockY}
        # The position of the anchor block (independent of rotation) in the field
        # Check which is the anchor block for every type
        self._anchor_pos = {'x': x, 'y': y}

    @classmethod
    def _determineAnchorBlockAndRotation(cls, type):
        if type == None:
            return -1, -1, 0
        elif type == cls.Type.I:
            return 0, 1, 90
        elif type == cls.Type.O: # Type.O is a special case. It can't be rotated.
            return 0, 0, 0
        elif type == cls.Type.T:
            return 1, 0, 0
        elif type == cls.Type.J:
            return 1, 0, 0
        elif type == cls.Type.L:
            return 1, 0, 0
        elif type == cls.Type.S:
            return 1, 1, -90
        elif type == cls.Type.Z:
            return 1, 1, 0

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

    @property
    def anchor_block(self):
        return self._anchor_block

    @anchor_block.setter
    def anchor_block(self, x, y):
        self._anchor_block['x'] = x
        self._anchor_block['y'] = y