#Peça ao usuário 5 números, guarde em um set, e mostre os números únicos digitados.
import tkinter as tk
from tkinter import ttk
numeros_usuario= { }
numeros_usuario=set(numeros_usuario)
def exibe_numero():
    label_numeros.config(text=numeros_usuario)
def adicionar_numero():
    numero=entry_menu.get()
    numeros_usuario.add(numero)

style=ttk.Style()
style.theme_use("alt")
style.configure('tButton',foreground="white",background="red",font="Arial")


janela= tk.Tk()
janela.title("set numeros")
janela.config(background="red")
janela.geometry("600x400")
entry_menu = tk.Entry(janela)
entry_menu.grid(column=0,row=1)
botao_numeros = tk.Button(janela, text="exiba numeros do usuario ",command=exibe_numero)
botao_numeros.grid(column=1,row=2)
botao_adicionar=tk.Button(janela,text="adicionar numero no set",command=adicionar_numero,padx=10,pady=10)
botao_adicionar.grid(column=5,row=5)
label_numeros=tk.Label(janela,text="")
label_numeros.grid(column=1,row=3)
janela.mainloop()