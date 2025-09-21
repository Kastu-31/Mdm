import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", ".txt"), ("All Files", ".*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", ".txt"), ("All Files", ".*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

# GUI setup
root = tk.Tk()
text = tk.Text(root)
text.pack()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)  # ✅ function name matches
file_menu.add_command(label="Save", command=save_file)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()