import arcade as Arcade

# Window size and title
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tetris"

# Window limits
TOP_Y = SCREEN_HEIGHT
BOTTOM_Y = 0
LEFT_X = 0
RIGHT_X = SCREEN_WIDTH

# Number of rows and columns.
NUM_ROWS = 20
NUM_COLS = 10

# Size (width) of a single block (a piece of a tetrimino).
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