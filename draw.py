import tkinter as tk
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill='blue')

root = tk.Tk()
root.title("Draw with little mouse")


canvas = tk.Canvas(root, width = 400, height = 400, bg = 'white')
canvas.pack()
canvas.bind("<B1-Motion>", draw)


root.mainloop()