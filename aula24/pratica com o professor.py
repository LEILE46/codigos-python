from tkinter import *
from tkinter import simpledialog,messagebox

janela= Tk()


def abrir_dialog():
    open=simpledialog.askstring("questao","o que entendeu?")
    if open.strip()== "entendi":
        messagebox.showinfo("resultado","muito bem,parabens")
    else:
        messagebox.showinfo("resultado","nao vc nao entendeu ")
btn= Button (text="dialog",command=abrir_dialog,background="lightpink")
btn.grid(row=4,column=2)


