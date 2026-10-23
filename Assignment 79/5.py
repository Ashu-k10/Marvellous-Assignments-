# Develop a tkinter application that accepts a username and password using Entry widgets. Provide a login button to validate the entered credentials against predefined values and display an appropriate success or failure message.

import tkinter as tk

def login():
    username = e1.get()
    password = e2.get()

    if username == "admin" and password == "1234":
        result.config(text="Login Successful!")
    else:
        result.config(text="Invalid Username or Password!")

root = tk.Tk()
root.title("Login Application")
root.geometry("300x200")

tk.Label(root, text="Username").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Password").pack()
e2 = tk.Entry(root, show="*")
e2.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()