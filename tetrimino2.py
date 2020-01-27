from enum import Enum
import arcade as Arcade
import block
from main import BLOCK_SIZE, AREA_LEFT, AREA_TOP

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
        self._rotation = self._determineInitialRotation(type)
        # The relative position of each dependent block to the anchor block.
        self._dependentBlocks = self._determineDependentBlocks(type)
        # The position of the anchor block (independent of rotation) in the field
        # Check which is the anchor block for every type
        self._anchor_pos = {'x': x, 'y': y}

    @classmethod
    def _determineInitialRotation(cls, type):
        if type == None:
            return 0
        elif type == cls.Type.I:
            return 90
        elif type == cls.Type.O: # Type.O is a special case. It can't be rotated.
            return 0
        elif type == cls.Type.T:
            return 0
        elif type == cls.Type.J:
            return 0
        elif type == cls.Type.L:
            return 0
        elif type == cls.Type.S:
            return 90
        elif type == cls.Type.Z:
            return 0

    @classmethod
    def _determineDependentBlocks(cls, type):
        if type == None:
            return []
        elif type == cls.Type.I:
            return [
                [0, -1],  # [ ]
                          # [X]
                [0,  1],  # [ ]
                [0,  2]   # [ ]
            ]
        elif type == cls.Type.O: # Type.O is a special case. It can't be rotated.
            return [
                        [1, 0], # [X][ ]
                [1, 0], [1, 1]  # [ ][ ]
            ]
        elif type == cls.Type.T:
            return [
                [-1, 0],        [1, 0],  #[ ][X][ ]
                         [0, 1]          #   [ ]
            ]
        elif type == cls.Type.J:
            return [
                [-1, -1],                 # [ ]
                [-1,  0],         [1, 0]  # [ ][X][ ]
            ]
        elif type == cls.Type.L:
            return [
                [-1, 0],         [1, 0]  # [ ][X][ ]
                [-1, 1],                 # [ ]
            ]
        elif type == cls.Type.S:
            return [
                [-1, -1],          # [ ]
                [-1,  0],          # [ ][X]
                          [0, -1]  #    [ ]
            ]
        elif type == cls.Type.Z:
            return [
                [-1, -1], [0, -1],          # [ ][ ]
                                   [1, 0]   #    [X][ ]
            ]

    # Rotate all the blocks.
    def rotate(self, degrees):
        # Left
        if degrees == -90:
            pass

        # Right
        elif degrees == 90:
            pass

    # Convert the whole tetrimino to a sprite list.
    # anchor_x and anchor_y are the position on the grid.
    # [0] is ALWAYS the anchor block.
    def to_sprite_list(self, anchor_x, anchor_y):
        sprites = Arcade.SpriteList()
        
        sprites.append(block.Block(self.type, center_x=AREA_LEFT + anchor_x * BLOCK_SIZE, center_y=AREA_TOP - anchor_y * BLOCK_SIZE))

        
        for i in range(len(self._dependentBlocks)):
            new_block = block.Block(self.type)
            new_block.center_x = sprites[0].center_x + BLOCK_SIZE * self._dependentBlocks[i][0]
            new_block.center_y = sprites[0].center_y - BLOCK_SIZE * self._dependentBlocks[i][1]
            sprites.append(new_block)
        
        return sprites
        


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