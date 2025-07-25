import tkinter.tix as tix
import tkinter.messagebox as mb

top = tix.Tk()
top.title("Tix Notebook Demo")

nb = tix.NoteBook(top, width=300, height=200)
nb.pack(expand=True, fill='both')

nb.add('page1', label="Text")
f1 = tix.Frame(nb.subwidget('page1'))
st = tix.ScrolledText(f1)
st.subwidget('text').insert("1.0", "Here is where the text goes...")
st.pack(expand=True)
f1.pack()

nb.add('page2', label="Message Boxes")
f2 = tix.Frame(nb.subwidget('page2'))

buttons = [
    ("error", "This is bad!", "lightblue", mb.showerror),
    ("info", "Information", "pink", mb.showinfo),
    ("warning", "Don't do it!", "yellow", mb.showwarning),
    ("question", "Will I?", "green", mb.askquestion),
    ("yes-no", "Are you sure?", "lightgrey", mb.askyesno),
    ("yes-no-cancel", "Last chance...", "black", mb.askyesnocancel)
]

for (txt, msg, color, func) in buttons:
    tix.Button(f2, text=txt, bg=color, fg='white' if color == "black" else 'black',
               command=lambda t=txt, m=msg, f=func: f(t, m)).pack(fill='x', expand=True)

f2.pack(side='top', fill='x')

top.mainloop()

