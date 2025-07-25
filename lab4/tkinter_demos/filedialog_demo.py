import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        messagebox.showinfo("Selected File", f"You selected:\n{file_path}")
    else:
        messagebox.showwarning("No File", "No file selected.")

root = tk.Tk()
root.title("FileDialog Demo")
root.geometry("300x150")

btn_open = tk.Button(root, text="Open File", command=open_file)
btn_open.pack(pady=40)

root.mainloop()
