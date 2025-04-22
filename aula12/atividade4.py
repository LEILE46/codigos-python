import tkinter as tk

pilha = []
tk.messagebox = tk.messagebox

def empilhar():
    valor = entrada.get()
    pilha.append(valor)
    entrada.delete(0, tk.END)
    atualizar()

def desempilhar():
    if pilha:
        valor = pilha.pop()
        tk.messagebox.showinfo("Desempilhado", f"Desempilhado: {valor}")
    else:
        tk.messagebox.showwarning("Aviso", "⚠️ Pilha vazia.")
    atualizar()

def ver_topo():
    if pilha:
        tk.messagebox.showinfo("Topo", f"Topo da pilha: {pilha[-1]}")
    else:
        tk.messagebox.showwarning("Aviso", "⚠️ Pilha vazia.")

def atualizar():
    pilha_label.config(text="Pilha: " + ', '.join(reversed(pilha)))

janela = tk.Tk()
janela.title("Menu Pilha")

entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Empilhar", command=empilhar).pack()
tk.Button(janela, text="Desempilhar", command=desempilhar).pack()
tk.Button(janela, text="Ver Topo", command=ver_topo).pack()

pilha_label = tk.Label(janela, text="Pilha:")
pilha_label.pack()

janela.mainloop()