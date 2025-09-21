import tkinter as tk
from tkinter import messagebox

def new_file():
    text_area.delete(1.0, tk.END)

    def open_file():
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())

    def save_file():
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt",                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text.get(1.0, tk.END))
            messagebox.showinfo("info", "File saved successfully!")

root = tk.Tk()
root.title("Simple Text Editor")    
root.geometry("600x400")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, wrap=tk.WORD, font=("helvetica", 12), fg="black", bg="white")
text.pack(expand=tk.yes, fill=tk.BOTH)

root.mainloop()