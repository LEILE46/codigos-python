#6. Pilha de nomes + busca

import tkinter as tk

pilha_nomes = []
tk.messagebox = tk.messagebox

def empilhar():
    nome = entrada.get()
    if nome.lower() == 'sair':
        janela.destroy()
    else:
        pilha_nomes.append(nome)
        entrada.delete(0, tk.END)
        atualizar()

def buscar():
    nome = entrada_busca.get()
    if nome in pilha_nomes:
        tk.messagebox.showinfo("Busca", "Nome encontrado!")
    else:
        tk.messagebox.showinfo("Busca", "Nome não está na pilha.")

def atualizar():
    pilha_label.config(text="Pilha: " + ', '.join(reversed(pilha_nomes)))

janela = tk.Tk()
janela.title("Pilha de Nomes")

entrada = tk.Entry(janela)
entrada.pack()
tk.Button(janela, text="Empilhar", command=empilhar).pack()

entrada_busca = tk.Entry(janela)
entrada_busca.pack()
tk.Button(janela, text="Buscar", command=buscar).pack()

pilha_label = tk.Label(janela, text="Pilha:")
pilha_label.pack()

janela.mainloop()