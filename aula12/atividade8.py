import tkinter as tk

def inverter():
    palavra = entrada.get()
    pilha = list(palavra)
    invertida = ''
    while pilha:
        invertida += pilha.pop()
    resultado.config(text="Invertida: " + invertida)

janela = tk.Tk()
janela.title("Inverter Palavra")
logo = tk.PhotoImage(file='aula12\\imagem\\imagem.png')
logo = logo.subsample(12,12)
lb_logo = tk.Label(janela, image=logo, background='#a83232')    
lb_logo.grid(row=0, column=0)

entrada = tk.Entry(janela)
entrada.grid(row=1, column=0)
tk.Button(janela, text="Inverter", command=inverter).grid(row=2, column=0)

resultado = tk.Label(janela, text="")
resultado.grid(row=3, column=0,pady=10)

janela.mainloop()
