import arcade as Arcade
import tetrimino, tetrimino2, block

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tetris"

TOP_Y = SCREEN_HEIGHT
BOTTOM_Y = 0
LEFT_X = 0
RIGHT_X = SCREEN_WIDTH

BLOCK_SIZE = 22
# The limits of the playing area (where blocks appear).
AREA_LEFT = 10
AREA_RIGHT = AREA_LEFT + BLOCK_SIZE * 10
AREA_BOTTOM = 10
AREA_TOP = AREA_BOTTOM + BLOCK_SIZE * 20

# Valid key bindings.
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

        # Individual blocks (pieces of tetriminos) in the grid
        self.blocks_list = None
        
        # Game area (with grid)
        self.game_area = None

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

    """ Game setup """
    def setup(self):
        self.player_list = Arcade.SpriteList()
        self.blocks_list = Arcade.SpriteList()

        # self.tetr = tetrimino.Tetrimino(tetrimino.Tetrimino.Type.S, 4, 0)
        self.tetr = tetrimino2.Tetrimino(tetrimino2.Tetrimino.Type.S, 4, 1)
        # self.player = Arcade.Sprite(filename=self.tetr.img)
        self.player_list = self.tetr.to_sprite_list()
        self.player = self.player_list[0]

        # TODO:
        # change this! (offset by half BLOCK_SIZE may not be final)
        """
        self.player.center_x = AREA_LEFT + self.tetr.anchor_pos['x'] * BLOCK_SIZE + BLOCK_SIZE / 2
        self.player.center_y = AREA_TOP - self.tetr.anchor_pos['y'] * BLOCK_SIZE - BLOCK_SIZE
        self.player.angle = self.tetr.rotation


        self.player_list.append(self.player)
        """
        # Game area (with grid)
        self.game_area = Arcade.ShapeElementList()
        self.game_area.append(Arcade.create_rectangle_outline(AREA_LEFT + (AREA_RIGHT - AREA_LEFT) / 2, AREA_BOTTOM + (AREA_TOP - AREA_BOTTOM) / 2, AREA_RIGHT - AREA_LEFT, AREA_TOP - AREA_BOTTOM, Arcade.color.WHITE, 2))

        for x in range(AREA_LEFT + BLOCK_SIZE, AREA_RIGHT, BLOCK_SIZE):
            self.game_area.append(Arcade.create_line(x, AREA_TOP, x, AREA_BOTTOM, (128, 128, 128, 128))) # Gray with 50% opacity
        
        for y in range(AREA_BOTTOM + BLOCK_SIZE, AREA_TOP, BLOCK_SIZE):
            self.game_area.append(Arcade.create_line(AREA_LEFT, y, AREA_RIGHT, y, (128, 128, 128, 128)))

        self.block = block.Block(tetrimino.Tetrimino.Type.I, 0, 0)
        self.block.position = 100, 100
        self.blocks_list.append(self.block)

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
            # TODO:
            # do this check with anchor_pos
            if self.player.center_x - self.player.width / 2 >= AREA_LEFT:
                self.player.change_x = -1 * BLOCK_SIZE
            self.left_pressed = False
        elif self.right_pressed and not self.left_pressed:
            if self.player.center_x + self.player.width / 2 <= AREA_RIGHT:
                self.player.change_x = BLOCK_SIZE
            self.right_pressed = False
        else:
            self.player.change_x = 0

        # Rotation
        if self.r_pressed:
            self.player.angle -= 90
            self.r_pressed = False

        self.player.center_x += self.player.change_x
        self.player.center_y += self.player.change_y

        # Show FPS
        print(1.0 / self.delta * 60)

    """ Render """
    def on_draw(self):
        Arcade.start_render()

        # Game area (with grid)
        self.game_area.draw()
        

        self.player_list.draw()
        self.blocks_list.draw()


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