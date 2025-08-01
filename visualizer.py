import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


def load_file():
    file_path = filedialog.askopenfilename()
    df = pd.read_csv(file_path)
    df.plot()
    plt.show()


root = tk.Tk()
root.title("CSV Data Visualizre")


btn = tk.Button(root, text="Load CSV & Plot", command=load_file)
btn.pack(pady=20)

root.mainloop()