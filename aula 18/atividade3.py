#Verifique se "banana" está na tupla.
import tkinter as tk
tupla_frutas=("maça","banana","laranja","pera","cereja")
janela= tk.Tk()
janela.title("tupla fruta")
janela.config(background="#2E40EC")
janela.geometry("600x400")

def exibi_fruta():
    if "banana" in tupla_frutas:
        label_frutas.config(text="tem banana na tupla")
    else:
        label_frutas.config(text="nao tem banana na tupla")
     


botao_frutas = tk.Button(janela, text="exiba frutas ",command=exibi_fruta)
botao_frutas.pack(side="top")

label_frutas=tk.Label(janela,text="")
label_frutas.pack(side="left")
janela.mainloop()