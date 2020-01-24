import arcade as Arcade

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tetris"
TOP_Y = SCREEN_HEIGHT
BOTTOM_Y = 0
LEFT_X = 0
RIGHT_X = SCREEN_WIDTH

class Game(Arcade.Window):
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)        
    
        self.player = None
        self.player_list = None

        Arcade.set_background_color(Arcade.color.WHITE)

    def setup(self):
        self.player = Arcade.Sprite(filename="char.gif")
        self.player.center_x = 150
        self.player.center_y = 450

        self.player_list = Arcade.SpriteList()
        self.player_list.append(self.player)


    """ Render """
    def on_draw(self):
        Arcade.start_render()
        self.player_list.draw()


    """ Tick """
    def update(self, delta_time):
        pass

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