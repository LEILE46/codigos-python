import tkinter as tk

tk.messagebox = tk.messagebox

def calcular():
    expr = entrada.get()
    tokens = expr.split()
    pilha = []

    try:
        for token in tokens:
            if token.isdigit():
                pilha.append(int(token))
            else:
                b = pilha.pop()
                a = pilha.pop()
                if token == '+': pilha.append(a + b)
                elif token == '-': pilha.append(a - b)
                elif token == '*': pilha.append(a * b)
                elif token == '/': pilha.append(a / b)
        resultado.config(text="Resultado: " + str(pilha[0]))
    except:
        tk.messagebox.showerror("Erro", "Expressão inválida.")

janela = tk.Tk()
janela.title("Calculadora RPN")

entrada = tk.Entry(janela)
entrada.pack()
tk.Button(janela, text="Calcular", command=calcular).pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()