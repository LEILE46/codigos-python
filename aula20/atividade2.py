#Remova uma fruta específica do set. Se a fruta não existir, não gerar erro (usar discard()).
import tkinter as tk
frutas_set={"maça","morango","banana","laranja","acerola"}

janela= tk.Tk()
janela.title("set fruta")
janela.config(background="blue")
janela.geometry("600x400")
def remover_fruta():
    entrada_usuario=entry_menu.get()
    frutas_set.discard(entrada_usuario)
    label_frutas.config(text=frutas_set)

frutas=tk.Label(text=frutas_set)
frutas.grid(column=0,row=0)   
entry_menu = tk.Entry(janela)
entry_menu.grid(column=0,row=1)
botao_frutas = tk.Button(janela, text="remover uma fruta ",command=remover_fruta)
botao_frutas.grid(column=1,row=2)
label_frutas=tk.Label(janela,text="")
label_frutas.grid(column=1,row=3)
janela.mainloop()