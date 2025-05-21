from tkinter import *
from tkinter import messagebox
from servicos.livro_serviços import *

def iniciar_interface(cursor, conn):
    janela = Tk()
    janela.title("📚 Livraria DB")
    janela.geometry("430x500")
    janela.configure(bg="#f0f0f0")

    font_padrao = ("Arial", 10)
    botao_cor = "#007acc"
    texto_cor = "white"

    Label(janela, text="Autor:", bg="#f0f0f0").place(x=30, y=20)
    autor_entry = Entry(janela, width=30)
    autor_entry.place(x=120, y=20)

    Label(janela, text="ID Livro:", bg="#f0f0f0").place(x=30, y=60)
    id_entry = Entry(janela, width=10)
    id_entry.place(x=120, y=60)

    Label(janela, text="Novo Preço:", bg="#f0f0f0").place(x=200, y=60)
    preco_entry = Entry(janela, width=10)
    preco_entry.place(x=290, y=60)

    def acao_exibir(): exibir_livros(cursor)
    def acao_pesquisar(): pesquisar_por_autor(cursor, autor_entry.get())
    def acao_atualizar():
        try:
            id_livro = int(id_entry.get())
            preco = float(preco_entry.get())
            atualizar_preco(cursor, conn, id_livro, preco)
        except:
            messagebox.showerror("Erro", "Digite ID e preço válidos.")
    def acao_remover():
        try:
            id_livro = int(id_entry.get())
            remover_livro(cursor, conn, id_livro)
        except:
            messagebox.showerror("Erro", "Digite um ID válido.")
    def acao_livros_autor(): livros_por_autor(cursor, autor_entry.get())
    def acao_desconto(): aplicar_desconto(cursor, conn)
    def acao_estoque(): relatorio_estoque(cursor)

    botoes = [
        ("📖 Exibir Todos os Livros", acao_exibir),
        ("🔍 Pesquisar Livros por Autor", acao_pesquisar),
        ("💰 Atualizar Preço de Livro", acao_atualizar),
        ("❌ Remover Livro", acao_remover),
        ("📚 Livros e Preços por Autor", acao_livros_autor),
        ("💸 Aplicar Desconto (> R$ 50)", acao_desconto),
        ("📦 Relatório de Estoque Zerado", acao_estoque),
    ]

    y_start = 110
    espacamento = 45

    for i, (texto, comando) in enumerate(botoes):
        Button(janela, text=texto, width=35, height=2, bg=botao_cor, fg=texto_cor, command=comando)\
            .place(x=60, y=y_start + i * espacamento)

    janela.mainloop()