import gui
import arcade as Arcade

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tetris"

class Game(Arcade.Window):
    
    player = None

    def __init__(self, width, height, title):
        super().__init__(width, height, title)        

        Arcade.set_background_color(Arcade.color.WHITE)
        # Arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tetris")
# gui.window = gui.create_window(title="Tetris", width=300, height=500)
# gui.canvas = gui.create_canvas()

    def setup(self):
        self.player = Player(, 1)

    """ Render """
    def on_draw(self):
        Arcade.start_render()



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
TOP_Y = 0
BOTTOM_Y = gui.canvas.winfo_reqheight()
LEFT_X = 0
RIGHT_X = gui.canvas.winfo_reqwidth()

r = gui.canvas.create_rectangle(50, 20, 150, 80, fill="green")

TICK_EVERY = 1 # seconds
DELTA_LIMIT = TICK_EVERY * 1000000000 # nanoseconds

"""