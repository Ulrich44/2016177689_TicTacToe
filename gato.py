from tkinter import *

ventana = Tk()
ventana.title("TIc Tic Toe")
ventana.minsize(600, 600)
ventana.resizable(width = FALSE, height = FALSE)
canvas = Canvas(ventana, width = 600, height = 600)
canvas.pack()
canvas.create_line(200, 0, 200, 600)
canvas.create_line(400, 0, 400, 600)
canvas.create_line(0, 200, 600, 200)
canvas.create_line(0, 400, 600, 400)
shape = "o"
grid = [
    "0", "1", "2",
    "3", "4", "5",
    "6", "7", "8",
]
def click(event):
    global shape, gid
    across = int(canvas.canvasx(event.x) / 200)
    down = int(canvas.canvasy(event.y) / 200)

    square = across + (down * 3)

    if grid[square] == "x" or grid[square] == "o":
        return
    if shape == "o":
        canvas.create_oval(across * 200, down *200, (across + 1) * 200, (down + 1) * 200)
        grid[square] = "o"
        shape = "x"
    else:
        canvas.create_line(across * 200, (down + 1) * 200, (across + 1) * 200, down * 200)
        canvas.create_line(across * 200, down * 200, (across + 1) * 200, (down + 1) * 200)
        grid[square] = "x"
        shape = "o"



canvas.bind("<Button-1>", click)
ventana.mainloop()

