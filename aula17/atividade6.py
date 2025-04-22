#Crie uma fila de compras (nomes de produtos). Ao remover, informe qual produto foi comprado.
import tkinter as  tk
fila_compra=["arroz","feijao","carne"]

def remover_produto():
    if fila_compra:
        produto_removido=fila_compra.pop(0)
        label_comprando.config(text=produto_removido)
    else:
       label_comprando.config(text= "fila vazia")





janela= tk.Tk()
janela.title("fila de compras")

label_atender_tarefa = tk.Label(janela, text="nome dos produtos:")
label_atender_tarefa.pack()
for produto in fila_compra:
    tk.Label(text=produto).pack()
botao_remover = tk.Button(janela, text="comprar ", command=remover_produto )
botao_remover.pack(side="top")
label_comprando=tk.Label(janela,text="")
label_comprando.pack()
janela.mainloop()