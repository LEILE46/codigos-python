import tkinter as tk

pilha = ['a', 'b', 'c']

def desempilhar():
    if not pilha:
        tk.messagebox.showwarning("Aviso", "⚠️ Pilha está vazia!")
    else:
        valor = pilha.pop()
        tk.messagebox.showinfo("Desempilhado", f"Valor desempilhado: {valor}")
        pilha_label.config(text="Pilha: " + ', '.join(reversed(pilha)))

janela = tk.Tk()
janela.title("Desempilhar")
tk.messagebox = tk.messagebox  # Habilita uso sem import direto

botao = tk.Button(janela, text="Desempilhar", command=desempilhar)
botao.pack()

pilha_label = tk.Label(janela, text="Pilha: " + ', '.join(reversed(pilha)))
pilha_label.pack()

janela.mainloop()