# Develop a tkinter application that accepts.persons name and age.Provide  a Check eligibility button to determine whether the person is eligible to vote based on minimum age of 18 years.

import tkinter as tk

def check_eligibility():
    name = e1.get()
    age = int(e2.get())

    if age >= 18:
        result.config(text=name + " is eligible to vote.")
    else:
        result.config(text=name + " is not eligible to vote.")

root = tk.Tk()
root.title("Voting Eligibility")
root.geometry("350x200")

tk.Label(root, text="Enter Name").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Enter Age").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Button(root, text="Check Eligibility",
          command=check_eligibility).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()