#Crie um set com 5 frutas. Adicione uma nova fruta e mostre o conjunto final.
import tkinter as tk
frutas_set={"maça","morango","banana","laranja","acerola"}

janela= tk.Tk()
janela.title("set fruta")
janela.config(background="yellow")
janela.geometry("600x400")
def exibi_fruta():
    frutas_set.add("uva")
    label_frutas.config(text=frutas_set)
frutas=tk.Label(text=frutas_set)
frutas.grid(column=0,row=0)   
botao_frutas = tk.Button(janela, text="exiba frutas ",command=exibi_fruta)
botao_frutas.grid(column=1,row=2)

label_frutas=tk.Label(janela,text="")
label_frutas.grid(column=1,row=3)
janela.mainloop()