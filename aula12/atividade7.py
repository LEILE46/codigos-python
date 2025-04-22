import tkinter as tk

navegador = []
tk.messagebox = tk.messagebox

def navegar():
    url = entrada.get()
    navegador.append(url)
    entrada.delete(0, tk.END)
    atualizar()

def voltar():
    if navegador:
        navegador.pop()
        atual = navegador[-1] if navegador else "Sem páginas"
        tk.messagebox.showinfo("Voltar", f"Página atual: {atual}")
    else:
        tk.messagebox.showwarning("Aviso", "⚠️ Nenhuma página para voltar.")
    atualizar()

def atualizar():
    label.config(text="Histórico: " + ' > '.join(navegador))

janela = tk.Tk()
janela.title("Navegador")

entrada = tk.Entry(janela)
entrada.pack()
tk.Button(janela, text="Navegar", command=navegar).pack()
tk.Button(janela, text="Voltar", command=voltar).pack()

label = tk.Label(janela, text="Histórico:")
label.pack()

janela.mainloop()