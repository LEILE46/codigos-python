import tkinter as tk

pilha = []

def empilhar():
    if len(pilha) >= 5:
        tk.messagebox.showinfo("Limite", "Máximo de 5 números.")
        return
    try:
        numero = int(entrada.get())
        pilha.append(numero)
        entrada.delete(0, tk.END)
        pilha_label.config(text="Pilha: " + ', '.join(map(str, pilha)))
        if len(pilha) == 5:
            tk.messagebox.showinfo("Topo", f"Topo da pilha: {pilha[-1]}")
    except ValueError:
        tk.messagebox.showerror("Erro", "Digite um número válido.")

janela = tk.Tk()
janela.title("Empilhador")

entrada = tk.Entry(janela)
entrada.pack(pady=5)

botao = tk.Button(janela, text="Empilhar", command=empilhar)
botao.pack(pady=5)

pilha_label = tk.Label(janela, text="Pilha: ")
pilha_label.pack(pady=5)

janela.mainloop()


    