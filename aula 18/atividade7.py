#Crie uma tupla com 5 letras. Exiba a tupla ordenada (use sorted(), que retorna lista).
import tkinter as tk
janela= tk.Tk()
janela.title("tupla 5 letras")
janela.config(background="#2E40EC")
janela.geometry("600x400")
tupla_nome=("z","a","e","w","n")
def ordena_nome():
    lista_nomes=list(tupla_nome)
    lista_nomes.sort()
    label_nome.config(text=lista_nomes)



botao_letras=tk.Button(janela, text="exibir letras ",command=ordena_nome)
botao_letras.grid(column=1,row=1,ipady=20)

label_nome=tk.Label(janela,text="")
label_nome.grid(column=2,row=1,pady=30,sticky="n",padx=20)
janela.mainloop()
