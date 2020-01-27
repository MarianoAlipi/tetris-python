# A single block of a tetrimino.

import arcade as Arcade
import tetrimino

BLOCK_SIZE = 22
AREA_LEFT = 10
AREA_BOTTOM = 10
AREA_TOP = AREA_BOTTOM + BLOCK_SIZE * 20

class Block(Arcade.Sprite):

    def __init__(self, type=None, anchor_x=-1, anchor_y=-1, center_x=0, center_y=0):
        self.type = type
        self.img = "assets/tetriminos/blocks/" + type.value + ".png"
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        super().__init__(filename=self.img, center_x=center_x, center_y=center_y)

    def update_position(self):
        self.center_x = AREA_LEFT + self.anchor_x * BLOCK_SIZE + BLOCK_SIZE / 2
        self.center_y = AREA_TOP  - self.anchor_y * BLOCK_SIZE - BLOCK_SIZE / 2