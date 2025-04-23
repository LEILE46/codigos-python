#Crie uma tupla com 3 nomes. Desempacote e exiba cada nome separadamente.
import tkinter as tk
janela= tk.Tk()
janela.title("tupla 3 nomes")
janela.config(background="#2E40EC")
janela.geometry("600x400")
tupla_nome=("erica","brenda","gaby")

def exiba_nome_separadamente():
    nome1,nome2,nome3=tupla_nome
    label_nome1=tk.Label(janela,text=nome1)
    label_nome1.grid(column=2,row=1,pady=10,sticky="s",padx=10)
    label_nome2=tk.Label(janela,text=nome2)
    label_nome2.grid(column=2,row=2,pady=10,sticky="s",padx=10)
    label_nome3=tk.Label(janela,text=nome3)
    label_nome3.grid(column=2,row=3,pady=10,sticky="s",padx=10)
       




botao_nomes=tk.Button(janela, text="exibir nomes ",command=exiba_nome_separadamente)
botao_nomes.grid(column=1,row=1,ipady=20)

label_nome=tk.Label(janela,text="")
label_nome.grid(column=2,row=1,pady=30,sticky="n",padx=20)
janela.mainloop()
