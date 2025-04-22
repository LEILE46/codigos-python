#5. Tamanho da pilha
import tkinter as tk

pilha = []

tk.messagebox = tk.messagebox

def empilhar():
    valor = entrada.get()
    pilha.append(valor)
    entrada.delete(0, tk.END)

def tamanho_pilha():
    tk.messagebox.showinfo("Tamanho", f"Tamanho da pilha: {len(pilha)}")

janela = tk.Tk()
janela.title("Tamanho da Pilha")

entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Empilhar", command=empilhar).pack()
tk.Button(janela, text="Ver Tamanho", command=tamanho_pilha).pack()

janela.mainloop()