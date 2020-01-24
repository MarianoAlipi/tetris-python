import arcade as Arcade

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tetris"
TOP_Y = SCREEN_HEIGHT
BOTTOM_Y = 0
LEFT_X = 0
RIGHT_X = SCREEN_WIDTH

class Game(Arcade.Window):
    
    """ Init """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)        
    
        self.player = None
        self.player_list = None
        self.delta = 0

        # Keys
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False

        Arcade.set_background_color(Arcade.color.WHITE)

    """ Setup """
    def setup(self):
        self.player = Arcade.Sprite(filename="char.gif")
        self.player.center_x = 150
        self.player.center_y = 450
        self.player.angle = 0

        self.player_list = Arcade.SpriteList()
        self.player_list.append(self.player)

    """ Tick """
    def update(self, delta_time):
        # Normalized delta time
        self.delta = delta_time * 60

        # Make player rotate (testing)
        # self.player.angle -= 360.0 / 120.0 * self.delta
        if self.up_pressed and not self.down_pressed:
            self.player.change_y = 3
        elif self.down_pressed and not self.up_pressed:
            self.player.change_y = -3
        else:
            self.player.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player.change_x = -3
        elif self.right_pressed and not self.left_pressed:
            self.player.change_x = 3
        else:
            self.player.change_x = 0

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
        if key == Arcade.key.UP:
            self.up_pressed = True
        elif key == Arcade.key.DOWN:
            self.down_pressed = True
        elif key == Arcade.key.LEFT:
            self.left_pressed = True
        elif key == Arcade.key.RIGHT:
            self.right_pressed = True
        elif key == Arcade.key.SPACE:
            self.space_pressed = True

    def on_key_release(self, key, modifiers):
        if key == Arcade.key.UP:
            self.up_pressed = False
        elif key == Arcade.key.DOWN:
            self.down_pressed = False
        elif key == Arcade.key.LEFT:
            self.left_pressed = False
        elif key == Arcade.key.RIGHT:
            self.right_pressed = False
        elif key == Arcade.key.SPACE:
            self.space_pressed = False

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