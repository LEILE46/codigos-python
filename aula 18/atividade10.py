#Desafio: Crie uma tupla de notas e calcule a média.
import tkinter as tk
janela= tk.Tk()
janela.title("tupla media")
janela.config(background="#2E40EC")
janela.geometry("600x400")
tupla_notas=(6,8,9,10)

def mostrar_media():
    somar1, somar2, somar3, somar4 = tupla_notas
    somar = somar1 + somar2 + somar3 + somar4
    divisao = somar / len(tupla_notas)
    label_numero.config(text=f"A soma da lista é de: {divisao}")



label_notas = tk.Label(janela, text=f"Notas: {tupla_notas}")
label_notas.grid(column=2,row=2,pady=30,sticky="n",padx=20)
botao_notas=tk.Button(janela, text="exibir media alunos",command=mostrar_media)
botao_notas.grid(column=1,row=1,ipady=20)

label_numero=tk.Label(janela,text="")
label_numero.grid(column=2,row=1,pady=30,sticky="n",padx=20)
janela.mainloop()



