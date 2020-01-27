import arcade as Arcade
import tetrimino, block
import constants as Const

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

        self.tetr = tetrimino.Tetrimino(tetrimino.Tetrimino.Type.Z, 4, 6)
        # self.player = Arcade.Sprite(filename=self.tetr.img)
        self.player_list = self.tetr.to_sprite_list()
        self.player = self.player_list[0]

        # TODO:
        # change this! (offset by half Const.BLOCK_SIZE may not be final)
        """
        self.player.center_x = Const.AREA_LEFT + self.tetr.anchor_pos['x'] * Const.BLOCK_SIZE + Const.BLOCK_SIZE / 2
        self.player.center_y = Const.AREA_TOP - self.tetr.anchor_pos['y'] * Const.BLOCK_SIZE - Const.BLOCK_SIZE
        self.player.angle = self.tetr.rotation


        self.player_list.append(self.player)
        """
        # Game area (with grid)
        self.game_area = Arcade.ShapeElementList()
        self.game_area.append(Arcade.create_rectangle_outline(Const.AREA_LEFT + (Const.AREA_RIGHT - Const.AREA_LEFT) / 2, Const.AREA_BOTTOM + (Const.AREA_TOP - Const.AREA_BOTTOM) / 2, Const.AREA_RIGHT - Const.AREA_LEFT, Const.AREA_TOP - Const.AREA_BOTTOM, Arcade.color.WHITE, 2))

        for x in range(Const.AREA_LEFT + Const.BLOCK_SIZE, Const.AREA_RIGHT, Const.BLOCK_SIZE):
            self.game_area.append(Arcade.create_line(x, Const.AREA_TOP, x, Const.AREA_BOTTOM, (128, 128, 128, 128))) # Gray with 50% opacity
        
        for y in range(Const.AREA_BOTTOM + Const.BLOCK_SIZE, Const.AREA_TOP, Const.BLOCK_SIZE):
            self.game_area.append(Arcade.create_line(Const.AREA_LEFT, y, Const.AREA_RIGHT, y, (128, 128, 128, 128)))

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
            if self.player.center_x - self.player.width / 2 >= Const.AREA_LEFT:
                self.tetr.move(-1, 0)
                self.player_list = self.tetr.to_sprite_list()
                self.player = self.player_list[0]
            self.left_pressed = False
        elif self.right_pressed and not self.left_pressed:
            if self.player.center_x + self.player.width / 2 <= Const.AREA_RIGHT:
                self.tetr.move(1, 0)
                self.player_list = self.tetr.to_sprite_list()
                self.player = self.player_list[0]
            self.right_pressed = False
        else:
            self.player.change_x = 0

        # Rotation
        if self.r_pressed:
            self.player.angle -= 90
            self.tetr.rotate(-90)
            self.player_list = self.tetr.to_sprite_list()
            self.player = self.player_list[0]
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
        if key in Const.UP_KEYS:
            self.up_pressed = True
        elif key in Const.DOWN_KEYS:
            self.down_pressed = True
        elif key in Const.LEFT_KEYS:
            self.left_pressed = True
        elif key in Const.RIGHT_KEYS:
            self.right_pressed = True
        elif key == Arcade.key.SPACE:
            self.space_pressed = True
        elif key == Arcade.key.R:
            self.r_pressed = True

    def on_key_release(self, key, modifiers):
        if key in Const.UP_KEYS:
            self.up_pressed = False
        elif key in Const.DOWN_KEYS:
            self.down_pressed = False
        elif key in Const.LEFT_KEYS:
            self.left_pressed = False
        elif key in Const.RIGHT_KEYS:
            self.right_pressed = False
        elif key == Arcade.key.SPACE:
            self.space_pressed = False
        elif key == Arcade.key.R:
            self.r_pressed = False

""" Main program """
def main():
    game = Game(Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT, Const.SCREEN_TITLE)
    game.setup()
    Arcade.run()

if __name__ == "__main__":
    main()

"""
TICK_EVERY = 1 # seconds
DELTA_LIMIT = TICK_EVERY * 1000000000 # nanoseconds
"""