import tkinter as tk
from tkinter import ttk
from servicos.operacao import listar_livros

def exibir_livros():
    janela = tk.Tk()
    janela.title("Livros Cadastrados")

    tree = ttk.Treeview(janela, columns=("ID", "Título", "Autor", "Preço", "Estoque"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Título", text="Título")
    tree.heading("Autor", text="Autor")
    tree.heading("Preço", text="Preço")
    tree.heading("Estoque", text="Estoque")

    for livro in listar_livros():
        tree.insert("", tk.END, values=livro)

    tree.pack(expand=True, fill='both')
    janela.mainloop()