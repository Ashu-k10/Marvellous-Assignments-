# Develop a tkinter application that accepts three numbers from the user. Provide a Find Maximum button to determine and display the largest number

import tkinter as tk
from tkinter import messagebox

def find_max():
    a = float(e1.get())
    b = float(e2.get())
    c = float(e3.get())

    maximum = max(a, b, c)
    result.config(text="Maximum Number: " + str(maximum))

root = tk.Tk()
root.title("Find Maximum")
root.geometry("300x300")

tk.Label(root, text="Enter First Number").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Enter Second Number").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Label(root, text="Enter Third Number").pack()
e3 = tk.Entry(root)
e3.pack()

tk.Button(root, text="Find Maximum",
          command=find_max).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()