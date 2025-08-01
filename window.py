import tkinter as tk

window = tk.Tk()
window.title("My First GUI")

label = tk.Label(window, text="Hello Mother Fucker!", font = ("Arial", 20))
label.pack(pady=20)
window.mainloop()