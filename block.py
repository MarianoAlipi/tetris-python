# A single block of a tetrimino.

import arcade as Arcade
import tetrimino

class Block(Arcade.Sprite):

    def __init__(self, type=None, x=-1, y=-1):
        self.type = type
        self.img = "assets/tetriminos/blocks/" + type.value + ".png"
        self.x = x
        self.y = y
        super().__init__(filename=self.img)