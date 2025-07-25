import tkinter as tk
from tkinter import ttk, messagebox

def create_notebook(root):
    notebook = ttk.Notebook(root)
    
    frame1 = ttk.Frame(notebook)
    text_widget = tk.Text(frame1, wrap="word", width=40, height=10)
    text_widget.insert("1.0", "Here is where the text goes...")
    text_widget.pack(expand=True, fill="both", padx=5, pady=5)
    notebook.add(frame1, text="Text")
    
    frame2 = ttk.Frame(notebook)
    buttons = [
        ("error", lambda: messagebox.showerror("error", "This is bad!")),
        ("info", lambda: messagebox.showinfo("info", "Information")),
        ("warning", lambda: messagebox.showwarning("warning", "Don't do it!")),
        ("question", lambda: messagebox.askquestion("question", "Will I?")),
        ("yes-no", lambda: messagebox.askyesno("yes-no", "Are you sure?")),
        ("yes-no-cancel", lambda: messagebox.askyesnocancel("yes-no-cancel", "Last chance...")),
    ]
    
    for text, cmd in buttons:
        ttk.Button(frame2, text=text, command=cmd).pack(fill='x', expand=True, padx=5, pady=2)
    
    notebook.add(frame2, text="Message Boxes")
    notebook.pack(expand=True, fill="both")

root = tk.Tk()
root.title("Notebook Demo (ttk)")
root.geometry("400x300")
create_notebook(root)
root.mainloop()

