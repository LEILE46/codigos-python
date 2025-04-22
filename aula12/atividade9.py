import tkinter as tk

tk.messagebox = tk.messagebox

def verificar():
    expr = entrada.get()
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in expr:
        if char in '([{':
            pilha.append(char)
        elif char in ')]}':
            if not pilha or pilha.pop() != pares[char]:
                tk.messagebox.showerror("Erro", "Parênteses incorretos.")
                return
    if not pilha:
        tk.messagebox.showinfo("Ok", "Parênteses corretos!")
    else:
        tk.messagebox.showerror("Erro", "Parênteses incorretos.")

janela = tk.Tk()
janela.title("Verificador de Parênteses")

entrada = tk.Entry(janela)
entrada.pack()
tk.Button(janela, text="Verificar", command=verificar).pack()

janela.mainloop()