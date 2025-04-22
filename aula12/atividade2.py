import tkinter as tk

pilha = []

def empilhar():
    valor = entrada.get()
    if valor.lower() == 'sair':
        janela.destroy()
    else:
        pilha.append(valor)
        entrada.delete(0, tk.END)
        pilha_label.config(text="Pilha: " + ', '.join(reversed(pilha)))

janela = tk.Tk()
janela.title("Empilhar até 'sair'")

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Empilhar", command=empilhar)
botao.pack()

pilha_label = tk.Label(janela, text="Pilha:")
pilha_label.pack()

janela.mainloop()