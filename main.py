import gui

gui.window = gui.create_window(title="Tetris", width=300, height=500)
gui.canvas = gui.create_canvas()

gui.canvas.create_rectangle(50, 20, 150, 80, fill="green")

input("Press ENTER to exit...")