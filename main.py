import gui
import time

gui.window = gui.create_window(title="Tetris", width=300, height=500)
gui.canvas = gui.create_canvas()

TOP_Y = 0
BOTTOM_Y = gui.canvas.winfo_reqheight()
LEFT_X = 0
RIGHT_X = gui.canvas.winfo_reqwidth()

r = gui.canvas.create_rectangle(50, 20, 150, 80, fill="green")
  
i = 1

input("Press ENTER to continue...")

TICK_EVERY = 1 # seconds
DELTA_LIMIT = TICK_EVERY * 1000000000 # nanoseconds

delta_time = 0.0
last_time = time.time_ns()

while True:

    current_time = time.time_ns()
    delta_time = delta_time + (current_time - last_time)
    last_time = current_time

    # If delta_time reached limit...
    if (delta_time >= DELTA_LIMIT):
        # Do tick
        print("Tick", i)
        i = i + 1

        # Reset delta_time
        delta_time = delta_time - DELTA_LIMIT



input("Press ENTER to exit...")