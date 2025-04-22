"""import tkinter as tk

def exibir_nomes():
    nomes = ["Ana", "João", "Carlos", "Maria", "Pedro"]
    for nome in nomes:
        listbox.insert(tk.END, nome)

root = tk.Tk()
root.title("Exibir Nomes")

listbox = tk.Listbox(root, height=6, width=20)
listbox.pack(pady=10)

button = tk.Button(root, text="Exibir Nomes", command=exibir_nomes)
button.pack(pady=5)

root.mainloop()"""
#atividade 2
"""import tkinter as tk

def calcular_media():
    numeros = [float(entry1.get()), float(entry2.get()), float(entry3.get()), float(entry4.get()), float(entry5.get())]
    media = sum(numeros) / len(numeros)
    label_resultado.config(text=f"Média: {media:.2f}")

root = tk.Tk()
root.title("Calcular Média")

label = tk.Label(root, text="Digite 5 números:")
label.pack(pady=10)

entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)
entry4 = tk.Entry(root)
entry4.pack(pady=5)
entry5 = tk.Entry(root)
entry5.pack(pady=5)

button = tk.Button(root, text="Calcular Média", command=calcular_media)
button.pack(pady=10)

label_resultado = tk.Label(root, text="Média: ")
label_resultado.pack(pady=10)

root.mainloop()"""
#3. Pedir 5 palavras e exibir a maior

"""import tkinter as tk

def exibir_maior_palavra():
    palavras = [entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get()]
    maior_palavra = max(palavras, key=len)
    label_resultado.config(text=f"A maior palavra é: {maior_palavra}")

root = tk.Tk()
root.title("Maior Palavra")

label = tk.Label(root, text="Digite 5 palavras:")
label.pack(pady=10)

entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)
entry4 = tk.Entry(root)
entry4.pack(pady=5)
entry5 = tk.Entry(root)
entry5.pack(pady=5)

button = tk.Button(root, text="Exibir Maior Palavra", command=exibir_maior_palavra)
button.pack(pady=10)

label_resultado = tk.Label(root, text="A maior palavra é: ")
label_resultado.pack(pady=10)

root.mainloop()""" 
#4. Ler 10 números e mostrar somente os pares

""""import tkinter as tk

def mostrar_pares():
    numeros = [int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get()), 
               int(entry6.get()), int(entry7.get()), int(entry8.get()), int(entry9.get()), int(entry10.get())]
    pares = [num for num in numeros if num % 2 == 0]
    listbox.delete(0, tk.END)
    for par in pares:
        listbox.insert(tk.END, par)

root = tk.Tk()
root.title("Mostrar Pares")

label = tk.Label(root, text="Digite 10 números:")
label.pack(pady=10)

entries = [tk.Entry(root) for _ in range(10)]
for entry in entries:
    entry.pack(pady=5)

button = tk.Button(root, text="Mostrar Pares", command=mostrar_pares)
button.pack(pady=10)

listbox = tk.Listbox(root, height=6, width=20)
listbox.pack(pady=10)

root.mainloop()""" 
#5. Pedir 5 produtos e adicionar em uma lista, depois remover um produto

"""import tkinter as tk

def adicionar_produto():
    produto = entry_produto.get()
    listbox_produtos.insert(tk.END, produto)
    entry_produto.delete(0, tk.END)

def remover_produto():
    produto_remover = entry_produto_remover.get()
    try:
        listbox_produtos.delete(listbox_produtos.get(0, tk.END).index(produto_remover))
    except ValueError:
        pass
    entry_produto_remover.delete(0, tk.END)

root = tk.Tk()
root.title("Gerenciar Produtos")

label_produto = tk.Label(root, text="Digite um produto:")
label_produto.pack(pady=5)
entry_produto = tk.Entry(root)
entry_produto.pack(pady=5)

button_adicionar = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
button_adicionar.pack(pady=5)

listbox_produtos = tk.Listbox(root, height=6, width=20)
listbox_produtos.pack(pady=10)

label_remover = tk.Label(root, text="Produto para remover:")
label_remover.pack(pady=5)
entry_produto_remover = tk.Entry(root)
entry_produto_remover.pack(pady=5)

button_remover = tk.Button(root, text="Remover Produto", command=remover_produto)
button_remover.pack(pady=5)

root.mainloop()"""
#6. Contar quantas idades são maiores que 18

import tkinter as tk

def contar_maiores_18():
    idades = [int(entry.get()) for entry in entries]
    maiores_18 = sum(1 for idade in idades if idade > 18)
    label_resultado.config(text=f"Maiores de 18: {maiores_18}")

janela = tk.Tk()
janela.title("Contar Maiores de 18")

label = tk.Label(janela, text="Digite 5 idades:")
label.pack(pady=10)
3
entries = []
for _ in range(5):
    entry = tk.Entry(janela)
    entry.pack(pady=5)
    entries.append(entry)
button = tk.Button(janela, text="Contar Maiores de 18", command=contar_maiores_18)
button.pack(pady=10)

label_resultado = tk.Label(janela, text="Maiores de 18: ")
label_resultado.pack(pady=10)

janela.mainloop()
#7. Verificar se um nome específico está na lista

"""import tkinter as tk

def verificar_nome():
    nomes = [entry.get() for entry in entries]
    nome_procurado = entry_nome_procurado.get()
    if nome_procurado in nomes:
        label_resultado.config(text=f"{nome_procurado} está na lista.")
    else:
        label_resultado.config(text=f"{nome_procurado} não está na lista.")

root = tk.Tk()
root.title("Verificar Nome")

label = tk.Label(root, text="Digite 7 nomes:")
label.pack(pady=10)

entries = [tk.Entry(root) for _ in range(7)]
for entry in entries:
    entry.pack(pady=5)

label_nome_procurado = tk.Label(root, text="Nome a procurar:")
label_nome_procurado.pack(pady=5)
entry_nome_procurado = tk.Entry(root)
entry_nome_procurado.pack(pady=5)

button = tk.Button(root, text="Verificar", command=verificar_nome)
button.pack(pady=10)

label_resultado = tk.Label(root, text="Resultado:")
label_resultado.pack(pady=10)

root.mainloop()"""
#8. Ordenar a lista de 5 números digitados

"""import tkinter as tk

def ordenar_numeros():
    numeros = [int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get())]
    numeros.sort()
    label_resultado.config(text=f"Números ordenados: {numeros}")

root = tk.Tk()
root.title("Ordenar Números")

label = tk.Label(root, text="Digite 5 números:")
label.pack(pady=10)

entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)
entry4 = tk.Entry(root)
entry4.pack(pady=5)
entry5 = tk.Entry(root)
entry5.pack(pady=5)

button = tk.Button(root, text="Ordenar Números", command=ordenar_numeros)
button.pack(pady=10)

label_resultado = tk.Label(root, text="Números ordenados:")
label_resultado.pack(pady=10)

root.mainloop()"""
#9. Exibir a maior e a menor nota de 6 notas

"""import tkinter as tk

def mostrar_maior_menor_nota():
    notas = [float(entry1.get()), float(entry2.get()), float(entry3.get()), float(entry4.get()), float(entry5.get()), float(entry6.get())]
    maior_nota = max(notas)
    menor_nota = min(notas)
    label_resultado.config(text=f"Maior nota: {maior_nota}, Menor nota: {menor_nota}")

root = tk.Tk()
root.title("Maior e Menor Nota")

label = tk.Label(root, text="Digite 6 notas:")
label.pack(pady=10)

entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)
entry4 = tk.Entry(root)
entry4.pack(pady=5)
entry5 = tk.Entry(root)
entry5.pack(pady=5)
entry6 = tk.Entry(root)
entry6.pack(pady=5)

button = tk.Button(root, text="Mostrar Notas", command=mostrar_maior_menor_nota)
button.pack(pady=10)

label_resultado = tk.Label(root, text="Resultado:")
label_resultado.pack(pady=10)

root.mainloop()"""
#10. Cadastrar nomes de alunos e encerrar quando "sair" for digitado

"""import tkinter as tk

def cadastrar_nome():
    nome = entry_nome.get()
    if nome.lower() == "sair":
        listbox_alunos.insert(tk.END, "Programa encerrado")
        root.quit()
    else:
        listbox_alunos.insert(tk.END, nome)
    entry_nome.delete(0, tk.END)

root = tk.Tk()
root.title("Cadastrar Alunos")

label = tk.Label(root, text="Digite o nome do aluno (ou 'sair' para encerrar):")
label.pack(pady=10)

entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

button = tk.Button(root, text="Cadastrar Nome", command=cadastrar_nome)
button.pack(pady=10)

listbox_alunos = tk.Listbox(root, height=6, width=30)
listbox_alunos.pack(pady=10)

root.mainloop()"""
