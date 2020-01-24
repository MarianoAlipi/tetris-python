import arcade as Arcade
import tetrimino

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tetris"
TOP_Y = SCREEN_HEIGHT
BOTTOM_Y = 0
LEFT_X = 0
RIGHT_X = SCREEN_WIDTH

UP_KEYS = [Arcade.key.UP, Arcade.key.W]
DOWN_KEYS = [Arcade.key.DOWN, Arcade.key.S]
LEFT_KEYS = [Arcade.key.LEFT, Arcade.key.A]
RIGHT_KEYS = [Arcade.key.RIGHT, Arcade.key.D]

class Game(Arcade.Window):
    
    """ Init """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)        
    
        # Player
        self.player = None
        self.player_list = None

        # Normalized delta time
        self.delta = 0

        # Keys
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False
        self.r_pressed = False

        # Field
        w, h = 10, 20
        self.field = [ [False for i in range(w)] for j in range(h) ]

        Arcade.set_background_color(Arcade.color.BLACK)

    """ Setup """
    def setup(self):
        self.tetr = tetrimino.Tetrimino(tetrimino.Tetrimino.Type.S, 0, 4)
        self.player = Arcade.Sprite(filename=self.tetr.img)
        self.player.center_x = 150
        self.player.center_y = 450
        self.player.angle = self.tetr.rotation

        self.player_list = Arcade.SpriteList()
        self.player_list.append(self.player)

    """ Tick """
    def update(self, delta_time):
        # Normalized delta time
        self.delta = delta_time * 60

        # Make player rotate (testing)
        # self.player.angle -= 360.0 / 120.0 * self.delta
        if self.up_pressed and not self.down_pressed:
            self.player.change_y = 4
        elif self.down_pressed and not self.up_pressed:
            self.player.change_y = -4
        else:
            self.player.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player.change_x = -4
        elif self.right_pressed and not self.left_pressed:
            self.player.change_x = 4
        else:
            self.player.change_x = 0

        # Rotation
        if self.r_pressed:
            self.player.angle -= 90
            self.r_pressed = False

        self.player.center_x += self.player.change_x
        self.player.center_y += self.player.change_y

    """ Render """
    def on_draw(self):
        Arcade.start_render()
        self.player_list.draw()
        self.player_list.draw()

    """ =================== """
    """ || Input manager || """
    """ =================== """
    def on_key_press(self, key, modifiers):
        if key in UP_KEYS:
            self.up_pressed = True
        elif key in DOWN_KEYS:
            self.down_pressed = True
        elif key in LEFT_KEYS:
            self.left_pressed = True
        elif key in RIGHT_KEYS:
            self.right_pressed = True
        elif key == Arcade.key.SPACE:
            self.space_pressed = True
        elif key == Arcade.key.R:
            self.r_pressed = True

    def on_key_release(self, key, modifiers):
        if key in UP_KEYS:
            self.up_pressed = False
        elif key in DOWN_KEYS:
            self.down_pressed = False
        elif key in LEFT_KEYS:
            self.left_pressed = False
        elif key in RIGHT_KEYS:
            self.right_pressed = False
        elif key == Arcade.key.SPACE:
            self.space_pressed = False
        elif key == Arcade.key.R:
            self.r_pressed = False

""" Main program """
def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    Arcade.run()

if __name__ == "__main__":
    main()

"""
TICK_EVERY = 1 # seconds
DELTA_LIMIT = TICK_EVERY * 1000000000 # nanoseconds
"""