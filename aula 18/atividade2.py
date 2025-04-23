#Acesse e exiba o 3º item da tupla de frutas.
import tkinter as tk
tupla_frutas=("maça","banana","laranja","pera","cereja")
janela= tk.Tk()
janela.title("tupla fruta")
janela.config(background="yellow")
janela.geometry("600x400")

def exibi_fruta():
    label_frutas.config(text=tupla_frutas[3])
     


botao_frutas = tk.Button(janela, text="exiba frutas ",command=exibi_fruta)
botao_frutas.pack(side="top")

label_frutas=tk.Label(janela,text="")
label_frutas.pack(side="left")
janela.mainloop()