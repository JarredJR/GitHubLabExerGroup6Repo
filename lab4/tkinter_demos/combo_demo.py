import tkinter as tk
from tkinter import ttk

def on_select(event):
    lab.config(text=f"Selected: {combo.get()}")

root = tk.Tk()
root.title("ComboBox Demo")

lab = tk.Label(root, text="Pick a value, any value...")
lab.pack(pady=10)

combo = ttk.Combobox(root, values=["Fred", "Ginger", "Gene", "Debbie", "Tommy"])
combo.current(0)
combo.bind("<<ComboboxSelected>>", on_select)
combo.pack(pady=5)

root.mainloop()
