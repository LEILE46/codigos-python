#Conte quantas vezes "maçã" aparece em uma tupla.
import tkinter as tk
tupla_frutas=("maça","banana","laranja","pera","cereja","maça")
janela= tk.Tk()
janela.title("tupla fruta")
janela.config(background="#2E40EC")
janela.geometry("600x400")

def exibi_fruta():
    tupla=tupla_frutas.count("maça")
    label_frutas.config(text=f"tem {tupla} maças")
     


botao_frutas = tk.Button(janela, text="exiba quantas vezes parece maça ",command=exibi_fruta)
botao_frutas.pack(side="top")

label_frutas=tk.Label(janela,text="")
label_frutas.pack(side="top",pady=30,anchor="s")
janela.mainloop()