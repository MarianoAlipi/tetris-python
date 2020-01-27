# A single block of a tetrimino.

import arcade as Arcade
import tetrimino

class Block(Arcade.Sprite):

    def __init__(self, type=None, anchor_x=-1, anchor_y=-1, center_x=0, center_y=0):
        self.type = type
        self.img = "assets/tetriminos/blocks/" + type.value + ".png"
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        super().__init__(filename=self.img, center_x=center_x, center_y=center_y)