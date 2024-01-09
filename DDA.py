import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def DDA(x0, y0, x1, y1):
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)
    steps = max(dx, dy)
    xinc = dx/steps
    yinc = dy/steps
    x = float(x0)
    y = float(y0)
    x_coordinates = []
    y_coordinates = []
    for i in range(steps):
        x_coordinates.append(x)
        y_coordinates.append(y)
        x = x + xinc
        y = y + yinc

    return x_coordinates, y_coordinates

def plot_dda(x_coordinates, y_coordinates):
    plt.plot(x_coordinates, y_coordinates,  markersize=1)
    plt.show()

def on_button_click(entry_x0, entry_y0, entry_x1, entry_y1):
    x0 = int(entry_x0.get())
    y0 = int(entry_y0.get())
    x1 = int(entry_x1.get())
    y1 = int(entry_y1.get())

    x_coordinates, y_coordinates = DDA(x0, y0, x1, y1)
    plot_dda(x_coordinates, y_coordinates)

def main():
    root = tk.Tk()
    root.title("DDA Line Drawing")

    # Create entry widgets for coordinates
    label_x0 = tk.Label(root, text="X0:")
    label_y0 = tk.Label(root, text="Y0:")
    label_x1 = tk.Label(root, text="X1:")
    label_y1 = tk.Label(root, text="Y1:")

    entry_x0 = tk.Entry(root)
    entry_y0 = tk.Entry(root)
    entry_x1 = tk.Entry(root)
    entry_y1 = tk.Entry(root)

    # Create a button to trigger the DDA algorithm
    button_draw = tk.Button(root, text="Draw Line", command=lambda: on_button_click(entry_x0, entry_y0, entry_x1, entry_y1))

    # Place widgets in the grid
    label_x0.grid(row=0, column=0)
    entry_x0.grid(row=0, column=1)
    label_y0.grid(row=1, column=0)
    entry_y0.grid(row=1, column=1)
    label_x1.grid(row=2, column=0)
    entry_x1.grid(row=2, column=1)
    label_y1.grid(row=3, column=0)
    entry_y1.grid(row=3, column=1)
    button_draw.grid(row=4, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()