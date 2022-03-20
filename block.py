# A single block of a tetrimino.

import arcade as Arcade

import constants as Const

class Block(Arcade.Sprite):

    # anchor_x and anchor_y are the positino in the actual field, NOT relative to anchor block.
    def __init__(self, type=None, anchor_x=-1, anchor_y=-1, center_x=0, center_y=0):
        self.type = type
        self.img = "assets/tetriminos/blocks/" + type.value + ".png"
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        super().__init__(filename=self.img, center_x=center_x, center_y=center_y)

    def update_position(self):
        self.center_x = Const.AREA_LEFT + self.anchor_x * Const.BLOCK_SIZE + Const.BLOCK_SIZE / 2
        self.center_y = Const.AREA_TOP  - self.anchor_y * Const.BLOCK_SIZE - Const.BLOCK_SIZE / 2
