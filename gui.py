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
    window.protocol("WM_DELETE_WINDOW", on_close)
    return window

# Create the canvas to draw on and add it to the window
def create_canvas():
    if (window != None):
        w, h = window.winfo_reqwidth(), window.winfo_reqheight()
        canvas = Canvas(window, width=w, height=h)
        canvas.pack()
        return canvas
    else:
        exit("ERROR: cannot create canvas because window has not been created.")
        return None

# Exit the program if the close button is clicked.
# This is just the behavior.
def on_close():
    exit()