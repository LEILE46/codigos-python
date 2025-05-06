import tkinter as tk
estoque = {}
 
def adicionar_produto():
    nome = entry_nome.get()
    quantidade = entry_qtd.get()
    try:
        if nome not in estoque:
            estoque[nome] = float(quantidade)
            label_estoque.config(text=f"Produto '{nome}' adicionado")
        else:
            label_estoque.config(text=f"O produto '{nome}' já existe. Use 'Atualizar'")
    except ValueError:
        label_estoque.config(text="Erro: Digite uma quantidade válida")
    limpar_campos()
 
def atualizar_quantidade():
    nome = entry_nome.get()
    quantidade = entry_qtd.get()
    try:
        if nome in estoque:
            estoque[nome] = float(quantidade)
            label_estoque.config(text=f"Quantidade de '{nome}' atualizada")
        else:
            label_estoque.config(text="Produto não encontrado")
    except ValueError:
        label_estoque.config(text="Erro: Digite uma quantidade válida")
    limpar_campos()
 
def remover_produto():
    nome = entry_nome.get()
    if nome in estoque:
        del estoque[nome]
        label_estoque.config(text=f"Produto '{nome}' removido.")
    else:
        label_estoque.config(text="Produto não encontrado.")
    limpar_campos()
 
def exibir_produtos():
    if estoque:
        texto = "Produtos disponíveis:\n"
        for nome, qtd in estoque.items():
            texto += f"{nome}: {qtd}\n"
    else:
        texto = "Estoque vazio."
    label_estoque.config(text=texto)
 
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)
 
janela = tk.Tk()
janela.title("Gerenciamento de Estoque")
janela.geometry("600x400")
janela.config(background="purple")
 
frame_entrada = tk.Frame(janela, bg="purple")
frame_entrada.grid(pady=10)
 
label_nome=tk.Label(frame_entrada, text="Nome:", bg="purple", fg="white")
label_nome.grid(row=0, column=0, padx=5)
entry_nome = tk.Entry(frame_entrada)
entry_nome.grid(row=0, column=1, padx=5)
 
label_quantidade=tk.Label(frame_entrada, text="Quantidade:", bg="purple", fg="white")
label_quantidade.grid(row=1, column=0, padx=5)
entry_qtd = tk.Entry(frame_entrada)
entry_qtd.grid(row=1, column=1, padx=5)
 
frame_botoes = tk.Frame(janela, bg="purple")
frame_botoes.grid(pady=5)
 
botao_adicionar=tk.Button(frame_botoes, text="Adicionar", width=15, command=adicionar_produto)
botao_adicionar.grid(row=0, column=0, padx=5)
botao_atualizar=tk.Button(frame_botoes, text="Atualizar", width=15, command=atualizar_quantidade)
botao_atualizar.grid(row=0, column=1, padx=5)
botao_remover=tk.Button(frame_botoes, text="Remover", width=15, command=remover_produto)
botao_remover.grid(row=1, column=0, padx=5, pady=5)
botao_exibir=tk.Button(frame_botoes, text="Exibir", width=15, command=exibir_produtos)
botao_exibir.grid(row=1, column=1, padx=5, pady=5)
 
frame_saida = tk.Frame(janela)
frame_saida.grid(pady=10,padx=60)
 
label_estoque = tk.Label(frame_saida, text="", bg="white", width=60, height=10, anchor="nw", justify="left")
label_estoque.grid()
 
janela.mainloop()