from enum import Enum
import arcade as Arcade
import block

BLOCK_SIZE = 22
# The limits of the playing area (where blocks appear).
AREA_LEFT = 10
AREA_BOTTOM = 10
AREA_TOP = AREA_BOTTOM + BLOCK_SIZE * 20

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
        self._dependentBlocksPos = self._determineDependentBlocks(type)
        # The position of the anchor block (independent of rotation) in the field
        # Check which is the anchor block for every type
        self._anchor_pos = {'x': x, 'y': y}
        # The dependent blocks (Block objects)
        self._dependentBlocks = []
        for i in range(len(self._dependentBlocksPos)):
            new_block = block.Block(self.type)
            new_block.anchor_x = self._anchor_pos['x'] + self._dependentBlocksPos[i][0]
            new_block.anchor_y = self._anchor_pos['y'] + self._dependentBlocksPos[i][1]
            self._dependentBlocks.append(new_block)

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
                # [ ]
                # [X]
                # [ ]
                # [ ]
            return [ [0, -1], [0,  1], [0,  2] ]
        elif type == cls.Type.O: # Type.O is a special case. It can't be rotated.
                # [X][ ]
                # [ ][ ]
            return [ [1, 0], [0, 1], [1, 1] ]
        elif type == cls.Type.T:
                # [ ][X][ ]
                #    [ ]
            return [ [-1, 0], [1, 0], [0, 1] ]
        elif type == cls.Type.J:
                # [ ]
                # [ ][X][ ]
            return [ [-1, -1], [-1, 0], [1, 0] ]
        elif type == cls.Type.L:
                # [ ][X][ ]
                # [ ]
            return [ [-1, 0], [1, 0], [-1, 1] ]
        elif type == cls.Type.S:
                # [ ]
                # [ ][X]
                #    [ ]
            return [ [-1, -1], [-1, 0], [0, 1] ]
        elif type == cls.Type.Z:
                # [ ][ ]
                #    [X][ ]
            return [ [-1, -1], [0, -1], [1, 0] ]

    # Rotate all the blocks.
    def rotate(self, degrees):
        # Left
        if degrees == -90:
            for i in range(len(self._dependentBlocks)):
                pair = self._dependentBlocksPos[i]
                if pair[0] > 0:
                    if pair[1] < 0:
                        pair = [-1 * pair[0], pair[1]]
                    elif pair[1] > 0:
                        pair = [pair[0], -1 * pair[1]]
                    else: # pair[1] == 0
                        pair = [0, -1 * pair[0]]
                elif pair[0] < 0:
                    if pair[1] < 0:
                        pair = [pair[0], -1 * pair[1]]
                    elif pair[1] > 0:
                        pair = [-1 * pair[0], pair[1]]
                    else: # pair[1] == 0
                        pair = [0, -1 * pair[0]]
                else: # pair[0] == 0
                    if pair[1] < 0:
                        pair = [pair[1], 0]
                    elif pair[1] > 0:
                        pair = [pair[1], 0]
                self._dependentBlocksPos[i] = pair
                self._dependentBlocks[i].anchor_x = self._anchor_pos['x'] + pair[0]
                self._dependentBlocks[i].anchor_y = self._anchor_pos['y'] + pair[1]
                self._dependentBlocks[i].update_position()
        # Right
        elif degrees == 90:
            pass

    # Move all the blocks.
    def move(self, x, y):
        self._anchor_pos['x'] += x
        self._anchor_pos['y'] += y

        for i in range(len(self._dependentBlocks)):
            new_block = self._dependentBlocks[i]
            new_block.anchor_x += x
            new_block.anchor_y += y
            self._dependentBlocks[i] = new_block
            self._dependentBlocks[i].update_position()

    # Convert the whole tetrimino to a sprite list.
    # [0] is ALWAYS the anchor block.
    def to_sprite_list(self):
        sprites = Arcade.SpriteList()
        
        sprites.append(block.Block(self.type, center_x=AREA_LEFT + self._anchor_pos['x'] * BLOCK_SIZE + BLOCK_SIZE / 2, center_y=AREA_TOP - self._anchor_pos['y'] * BLOCK_SIZE - BLOCK_SIZE / 2))
        
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