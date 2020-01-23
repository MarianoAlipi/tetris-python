from tkinter import Tk, Canvas
from enum import Enum

window = None
canvas = None
scale = None


# Scale of the render
class GuiScale(Enum):
    X1 = 1
    X2 = 2

# Create the main window
# Optional parameters:
#   title
#   width
#   height
def create_window(**kwargs):
    scale = GuiScale.X1
    window = Tk()
    window.title(kwargs.get('title', ""))
    window.minsize(kwargs.get('width', 300 * scale.value), kwargs.get('height', 300 * scale.value))
    window.maxsize(kwargs.get('width', 300 * scale.value), kwargs.get('height', 300 * scale.value))
    return window

# Create the canvas to draw on and add it to the window
def create_canvas():
    if (window != None):
        w, h = window.size()
        canvas = Canvas(window, width=w, height=h)
        canvas.pack()
        return canvas
    else:
        exit("ERROR: cannot create canvas because window has not been created.")
        return None


window = create_window(title="Tetris", width=300, height=500)
canvas = create_canvas()

input("Press a key to exit...")