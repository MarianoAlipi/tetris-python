from enum import Enum

import arcade as Arcade

import block
import constants as Const


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
        # The relative position of each dependent block to the anchor block.
        self._dependentBlocksPos = self._determineDependentBlocks(type)
        # The position of the anchor block (independent of rotation) in the field
        if x != -1 and y != -1:
            self._anchor_pos = {'x': x, 'y': y}
        else:
            self._anchor_pos = {'x': 4, 'y': 1 if type == Tetrimino.Type.S or type == Tetrimino.Type.Z else 0}
        # The dependent blocks (Block objects)
        self._dependentBlocks = []
        for i in range(len(self._dependentBlocksPos)):
            new_block = block.Block(self.type)
            new_block.anchor_x = self._anchor_pos['x'] + self._dependentBlocksPos[i][0]
            new_block.anchor_y = self._anchor_pos['y'] + self._dependentBlocksPos[i][1]
            self._dependentBlocks.append(new_block)

    @classmethod
    def _determineDependentBlocks(cls, type):
        if type == None:
            return []
        elif type == cls.Type.I:
                # [ ][X][ ][ ]
            return [ [-1, 0], [1, 0], [2, 0] ]
        elif type == cls.Type.O: # Type.O is a special case. It can't be rotated.
                # [X][ ]
                # [ ][ ]
            return [ [1, 0], [0, 1], [1, 1] ]
        elif type == cls.Type.T:
                # [ ][X][ ]
                #    [ ]
            return [ [-1, 0], [1, 0], [0, 1] ]
        elif type == cls.Type.J:
                # [ ][X][ ]
                #       [ ]
            return [ [-1, 0], [1, 0], [1, 1] ]
        elif type == cls.Type.L:
                # [ ][X][ ]
                # [ ]
            return [ [-1, 0], [1, 0], [-1, 1] ]
        elif type == cls.Type.S:
                #    [ ][ ]
                # [ ][X]
            return [ [0, -1], [1, -1], [-1, 0] ]
        elif type == cls.Type.Z:
                # [ ][ ]
                #    [X][ ]
            return [ [-1, -1], [0, -1], [1, 0] ]

    # Convert the whole tetrimino to a sprite list.
    # [0] is ALWAYS the anchor block.
    def to_sprite_list(self):
        sprites = Arcade.SpriteList()
        
        sprites.append(block.Block(self.type, anchor_x=self.anchor_pos['x'], anchor_y=self.anchor_pos['y'], center_x=Const.AREA_LEFT + self._anchor_pos['x'] * Const.BLOCK_SIZE + Const.BLOCK_SIZE / 2, center_y=Const.AREA_TOP - self._anchor_pos['y'] * Const.BLOCK_SIZE - Const.BLOCK_SIZE / 2))
        
        for i in range(len(self._dependentBlocks)):
            new_block = self._dependentBlocks[i]
            new_block.update_position()
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
