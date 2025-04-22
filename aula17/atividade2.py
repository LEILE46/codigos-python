#Permita que o usuário insira quantos nomes quiser. Use "sair" como condição para parar. Ao final, mostre a fila.
import tkinter as tk
fila=[]
 
def adicionar_nome():
    while True:
        nome=entry_nome.get()
        if nome == "sair":
            label_resultado= tk.Label(text="voce saiu do sistema")
            label_resultado.pack()
            label_resultadofinal=tk.Label(text=f"a sua fila e {fila}")
            label_resultadofinal.pack()
            break
        else:
            fila.append(nome)
            break
        
           

janela = tk.Tk()
janela.title("Fila de Nomes")

label_nome = tk.Label(janela, text="Digite o nome (ou 'sair' para encerrar):")
label_nome.pack()

entry_nome = tk.Entry(janela)
entry_nome.pack()

botao_adicionar = tk.Button(janela, text="Adicionar", command=adicionar_nome)
botao_adicionar.pack()


janela.mainloop()
