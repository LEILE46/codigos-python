#Simule uma fila de senhas de atendimento. Cada novo nome recebe uma senha numérica sequencial.
import tkinter as tk
nome_lista=[]
def gerar_senha():
    nome=entry_senha.get()
    nome_lista.append(nome)
    for i in range (len(nome_lista)):
        label_senha.config(text=f" o cliente {nome} pegou a senha {i}")


janela = tk.Tk()
janela.title("fila de senhas")

label_senha = tk.Label(janela, text="escreva seu nome:")
label_senha.pack()

entry_senha = tk.Entry(janela)
entry_senha.pack()

botao_adicionar = tk.Button(janela, text="pegar senha ", command=gerar_senha)
botao_adicionar.pack()


janela.mainloop()
