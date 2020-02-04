"""
TODO:
    make rotation look for a free space when it's too tight.
    
    Currently this causes the T tetrimino (maybe others) to get
    stuck at the top if they're rotated right after they appear.

"""

import arcade as Arcade

import block
import constants as Const
import tetrimino


class Game(Arcade.Window):
    
    """ ========== """
    """ || Init || """
    """ ========== """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)        
    
        # Background color
        Arcade.set_background_color(Arcade.color.BLACK)

        # Field
        self.field = [ [None for i in range(Const.NUM_COLS)] for j in range(Const.NUM_ROWS) ]
        
        # Player (the current tetrimino)
        # tetrimino is a Tetrimino object converted to sprite_list.
        self.tetrimino = None

        # Individual blocks (pieces of tetriminos) in the grid
        self.blocks_list = None
        self.debug_list = None

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
        
        # Fall speed (move down by one block every # frames)
        # Default: 50
        self.fall_every = 50
        self.fall_counter = 0

    """ ================ """
    """ || Game setup || """
    """ ================ """
    def setup(self):

        self.tetrimino = Arcade.SpriteList()
        self.blocks_list = Arcade.SpriteList()

        # The tallest occupied space by column.
        # The lower the number, the higher the block is on the screen.
        self.max_by_col = self.find_max_by_col()

        self.tetrimino = tetrimino.Tetrimino(type=tetrimino.Tetrimino.Type.S).to_sprite_list()
        self.add_tetrimino_to_field(self.tetrimino)


        # Game area (with grid)
        self.game_area = Arcade.ShapeElementList()
        self.game_area.append(Arcade.create_rectangle_outline(Const.AREA_LEFT + (Const.AREA_RIGHT - Const.AREA_LEFT) / 2, Const.AREA_BOTTOM + (Const.AREA_TOP - Const.AREA_BOTTOM) / 2, Const.AREA_RIGHT - Const.AREA_LEFT, Const.AREA_TOP - Const.AREA_BOTTOM, Arcade.color.WHITE, 2))

        for x in range(Const.AREA_LEFT + Const.BLOCK_SIZE, Const.AREA_RIGHT, Const.BLOCK_SIZE):
            self.game_area.append(Arcade.create_line(x, Const.AREA_TOP, x, Const.AREA_BOTTOM, (128, 128, 128, 128))) # Gray with 50% opacity
        
        for y in range(Const.AREA_BOTTOM + Const.BLOCK_SIZE, Const.AREA_TOP, Const.BLOCK_SIZE):
            self.game_area.append(Arcade.create_line(Const.AREA_LEFT, y, Const.AREA_RIGHT, y, (128, 128, 128, 128)))

    """ ========== """
    """ || Tick || """
    """ ========== """
    def update(self, delta_time):
        # Normalized delta time
        self.delta = delta_time * 60

        print("Max list: ", end="")
        for val in self.max_by_col:
            print(val, end=" ")
        print()

        if self.up_pressed and not self.down_pressed:
            #self.player.change_y = 4
            pass
        elif self.down_pressed and not self.up_pressed:
            #self.player.change_y = -4
            pass
        else:
            #self.player.change_y = 0
            pass

        """ Horizontal movement """
        # Left
        if self.left_pressed and not self.right_pressed:
            # If it can still move left...
            if self.tetrimino[0].anchor_x - 1 >= 0:
                self.move_tetrimino(self.tetrimino, -1, 0)
            # Release (reset) key
            self.left_pressed = False
        # Right
        elif self.right_pressed and not self.left_pressed:
            # If it can still move right...
            if self.tetrimino[0].anchor_x + 1 < Const.NUM_COLS:
                self.move_tetrimino(self.tetrimino, 1, 0)
            # Release (reset) key
            self.right_pressed = False

        """ Rotation """
        if self.r_pressed:
            # Check it's not the O tetrimino (it can't rotate).
            if self.tetrimino[0].type != tetrimino.Tetrimino.Type.O:
                self.rotate_tetrimino(self.tetrimino, 90)
            self.r_pressed = False

        """ Gravity """
        if self.fall_counter >= self.fall_every:
            # Attempt to move down
            if self.move_tetrimino(self.tetrimino, 0, 1):
                # Success
                pass
            else:
                # Failure
                # Convert tetrimino to blocks.
                for blk in self.tetrimino:
                    self.blocks_list.append(blk)
                # Update maximum height
                self.max_by_col = self.find_max_by_col()
                # Create new tetrimino.
                self.tetrimino = tetrimino.Tetrimino(type=tetrimino.Tetrimino.Type.T).to_sprite_list()
                self.add_tetrimino_to_field(self.tetrimino)
            self.fall_counter = 0
        else:
            self.fall_counter += 1

        # Show FPS
        print(1.0 / self.delta * 60)

    """ ============ """
    """ || Render ||"""
    """ ============ """
    def on_draw(self):
        Arcade.start_render()

        # Game area (with grid)
        self.game_area.draw()

        # The current tetrimino
        self.tetrimino.draw()

        # The blocks already placed
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

    """ ================================== """
    """ || Utils and tetrimino handling ||"""
    """ ================================== """

    """ Check a position in the field is valid and empty. 
        tetr is the tetrimino to which the block belongs, in order to ignore it.
    """
    def check_valid_and_empty(self, x=-1, y=-1, tetr=[]):
        # Check it's inside the game area.
        if x >= 0 and x < Const.NUM_COLS and y >= 0 and y < Const.NUM_ROWS:
            # Check there isn't already a block in the target position.
            return (self.field[y][x] == None) or (self.field[y][x] in tetr)
        # It's outside the game area.
        else:
            return False

    """ Add the tetrimino's blocks to the field matrix. """
    def add_tetrimino_to_field(self, tetr):
        for blk in tetr:
            x = blk.anchor_x
            y = blk.anchor_y

            self.field[y][x] = blk

    """ Move a tetrimino (SpriteList). """
    def move_tetrimino(self, tetr, x=0, y=0):
        # The target anchor positions of each block will be stored in these lists.
        # If every block can be moved, the blocks' new anchor_x and y will be
        # the values in these lists.
        backup_anchors_x = []
        backup_anchors_y = []

        # Check if every block can be moved.
        for blk in tetr:

            # Target anchor position.
            new_x = blk.anchor_x + x
            new_y = blk.anchor_y + y

            if self.check_valid_and_empty(new_x, new_y, tetr):
                backup_anchors_x.append(new_x)
                backup_anchors_y.append(new_y)
            # One of the blocks cannot move. Exit the function.
            else:
                return False

        # All the blocks have been checked and they CAN move.
        # Remove them all from the field.
        # Separated for loops to avoid erasing a new block.
        for blk in tetr:
            # Remove from field.
            self.field[blk.anchor_y][blk.anchor_x] = None

        i = 0
        for blk in tetr:
            # Update position values.
            blk.anchor_x = backup_anchors_x[i]
            blk.anchor_y = backup_anchors_y[i]
            blk.update_position()
            # Add to field with new position.
            self.field[blk.anchor_y][blk.anchor_x] = blk

            i += 1
        
        return True

    """ Rotate a tetrimino (SpriteList). """
    def rotate_tetrimino(self, tetr, degrees=0):
        is_first = True
        anchor_block = tetr[0]

        # The target anchor positions of each block will be stored in these lists.
        # If every block can be moved, the blocks' new anchor_x and y will be
        # the values in these lists.
        backup_anchors_x = []
        backup_anchors_y = []

        # Left
        if degrees == -90:
            for blk in tetr:

                if is_first:
                    is_first = False
                    continue

                pair = [blk.anchor_x - anchor_block.anchor_x, blk.anchor_y - anchor_block.anchor_y]

                if pair[0] > 0:
                    if pair[1] < 0:
                        pair = [-1 * pair[0], pair[1]]
                    elif pair[1] > 0:
                        pair = [pair[0], -1 * pair[1]]
                    else: # pair[1] == 0
                        pair = [0, -1 * pair[0]]
                elif pair[0] < 0:
                    if pair[1] < 0:
                        pair = [pair[0], -1 * pair[1]]
                    elif pair[1] > 0:
                        pair = [-1 * pair[0], pair[1]]
                    else: # pair[1] == 0
                        pair = [0, -1 * pair[0]]
                else: # pair[0] == 0
                    if pair[1] < 0:
                        pair = [pair[1], 0]
                    elif pair[1] > 0:
                        pair = [pair[1], 0]

                new_x = anchor_block.anchor_x + pair[0]
                new_y = anchor_block.anchor_y + pair[1]

                if self.check_valid_and_empty(new_x, new_y, tetr):
                    backup_anchors_x.append(new_x)
                    backup_anchors_y.append(new_y)
                else:
                    # Can't move this block.
                    return False

        # Right
        elif degrees == 90:
            for blk in tetr:

                if is_first:
                    is_first = False
                    continue

                pair = [blk.anchor_x - anchor_block.anchor_x, blk.anchor_y - anchor_block.anchor_y]

                if pair[0] > 0:
                    if pair[1] < 0:
                        pair = [pair[0], -1 * pair[1]]
                    elif pair[1] > 0:
                        pair = [-1 * pair[0], pair[1]]
                    else: # pair[1] == 0
                        pair = [0, pair[0]]
                elif pair[0] < 0:
                    if pair[1] < 0:
                        pair = [-1 * pair[0], pair[1]]
                    elif pair[1] > 0:
                        pair = [pair[0], -1 * pair[1]]
                    else: # pair[1] == 0
                        pair = [0, pair[0]]
                else: # pair[0] == 0
                    if pair[1] < 0:
                        pair = [-1 * pair[1], 0]
                    elif pair[1] > 0:
                        pair = [-1 * pair[1], 0]
                        
                new_x = anchor_block.anchor_x + pair[0]
                new_y = anchor_block.anchor_y + pair[1]

                if self.check_valid_and_empty(new_x, new_y, tetr):
                    backup_anchors_x.append(new_x)
                    backup_anchors_y.append(new_y)
                else:
                    # Can't move this block.
                    return False

        # If the program reaches this point, every block can be moved.
        # Move them (skip the first one).

        # Remove them all from the field.
        # Separated for loops to avoid erasing a new block.
        i = 0
        for blk in tetr:
            if i == 0:
                i += 1
                continue

            # Remove from field.
            self.field[blk.anchor_y][blk.anchor_x] = None

        i = 0
        for blk in tetr:
            if i == 0:
                i += 1
                continue

            # Update position values.
            blk.anchor_x = backup_anchors_x[i - 1]
            blk.anchor_y = backup_anchors_y[i - 1]
            blk.update_position()
            # Add to field with new position.
            self.field[blk.anchor_y][blk.anchor_x] = blk

            i += 1

        return True

    """ Find the tallest occupied point (anchor_y) in the field for every column and return it. """
    """ Ignore tetrimino passed as optional parameter 'ignore'. """
    """ This is inneficient. It must be used only to setup. """
    def find_max_by_col(self, ignore=[]):

        # Make every column's max be below the lowest row (10).
        by_col = [Const.NUM_ROWS for i in range(Const.NUM_COLS)]

        for y in range(Const.NUM_ROWS):
            for x in range(Const.NUM_COLS):
                if self.field[y][x] != None:
                    if self.field[y][x] not in ignore:
                        if y < by_col[x]:
                            by_col[x] = y

        return by_col

    """ Check the rows a tetrimino is in (ideally just as it lands) for fully occupied rows. """
    def check_full_rows(self, tetr=[]):

        rows = []
        full_rows = []

        # Add the rows affected by the tetrimino to the list.
        for blk in tetr:
            if blk.anchor_y not in rows:
                rows.append(blk.anchor_y)

        # Check if each row is full.
        for row in rows:
            is_full = True

            for i in range(Const.NUM_COLS):
                if self.field[row][i] == None:
                    is_full = False
                    break
            
            if is_full:
                full_rows.append(row)

        # Return the full rows.
        return full_rows

    """ Remove all the blocks in the rows and move everything above them down. Ignore the blocks of the current tetrimino 'tetr'. """
    def clear_rows(self, rows=[], tetr=[]):

        for row in rows:
            for col in range(Const.NUM_COLS):
                if self.field[row][col] not in tetr:
                    self.field[row][col] = None
                
        # WIP #
        # WIP #
        # WIP #
        # Move everything down

            

""" ================== """
""" || Main program || """
""" ================== """
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
