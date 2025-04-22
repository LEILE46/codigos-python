#Implemente um menu com as opções: adicionar, remover, visualizar fila, limpar fila, sair.
import tkinter as tk
fila_menu=[]
def opcao_adicionar():
    
    nome=entry_menu.get()
    if nome:
        fila_menu.append(nome)
        label_resultado.config(text=f"{nome} foi adicionado.")

def remover_nome():
    if fila_menu:
        nome_removido = fila_menu.pop(0)
        label_resultado.config(text=f"{nome_removido} foi removido da fila.")
    else:
        label_resultado.config(text="A fila está vazia.")

def visualizar_fila():
    if len(fila_menu) > 0:
        label_resultado.config(text="")
    else:
        label_resultado.config(text="A fila está vazia.")


def limpar_fila():
    fila_menu.clear()
    label_resultado.config(text="Fila limpa com sucesso.")


janela= tk.Tk()
janela.title("menu")

label_menu = tk.Label(janela, text="menus:")
label_menu.pack()

entry_menu = tk.Entry(janela)
entry_menu.pack()
botao_adicionar = tk.Button(janela, text="adicionar ", command=opcao_adicionar)
botao_adicionar.pack()
botao_remover=tk.Button (janela,text="remover",command=remover_nome)
botao_remover.pack()
botao_vizualizar=tk.Button(janela,text="vizualizar fila",command=visualizar_fila)
botao_vizualizar.pack()
botao_limpar=tk.Button(janela,text="limpar fila",command=limpar_fila)
botao_limpar.pack()
botao_sair=tk.Button(janela,text="")
botao_sair.pack()
label_resultado = tk.Label(janela, text="", wraplength=280, justify="left")
label_resultado.pack(pady=10)
janela.mainloop()
