import tkinter as tk
import algorithm as algo

root = tk.Tk()
root.geometry("300x170")

title_label = tk.Label(root, text="Random password generator", font=("Arial", 16))
title_label.pack()

hint_entry = tk.Entry(root)
hint_entry.pack()

generate_btn = tk.Button(root, text="Generate", command=algo.generate_func)
generate_btn.pack()

generated_psw = tk.Label(root, font=("Arial", 13))
generated_psw.pack()

copy_btn = tk.Button(root, text="Copy", command=algo.copy_func)
copy_btn.pack()

reset_btn = tk.Button(root, text="Reset", command=algo.reset_func)
reset_btn.pack()

root.mainloop()