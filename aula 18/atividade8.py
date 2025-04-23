#Crie uma tupla com dados de um aluno: nome, idade e curso. Mostre cada dado com print().
import tkinter as tk
janela= tk.Tk()
janela.title("tupla 5 letras")
janela.config(background="#2E40EC")
janela.geometry("600x400")
tupla_nome=("eliane","26","desenvolvedor de sistemas")

def dados():
    nome, ida, cur=tupla_nome
    label_nome.config(text=f'nome e {nome}, idade e {ida}, curso {cur}')



botao_letras=tk.Button(janela, text="exibir dados aluno ",command=dados)
botao_letras.grid(column=1,row=1,ipady=20)

label_nome=tk.Label(janela,text="")
label_nome.grid(column=2,row=1,pady=30,sticky="n",padx=20)
janela.mainloop()