# Develop a tkinter application that accepts the radius of a circle. Provide a Calculate Area button to calculate and display area of the circle

import tkinter as tk
import math

def calculate_area():
    r = float(entry.get())
    area = math.pi * r * r
    result.config(text="Area: " + str(round(area, 2)))

root = tk.Tk()
root.title("Circle Area")
root.geometry("300x200")

tk.Label(root, text="Enter Radius").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate Area",
          command=calculate_area).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()