# develop a tkinter application that accepts two numbers using entry widgets. provide an add button to calculate and display their addtion using a label widget

import tkinter as tk

def add():
    n1 = int(e1.get())
    n2 = int(e2.get())

    result = n1 + n2
    lbl_result.config(text="Addition = " + str(result))

root = tk.Tk()
root.title("Addition Calculator")
root.geometry("300x250")

tk.Label(root, text="Enter First Number").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Enter Second Number").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Button(root, text="Add", command=add).pack(pady=10)

lbl_result = tk.Label(root, text="Addition = ")
lbl_result.pack()

root.mainloop()
