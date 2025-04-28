#Crie duas tuplas com números e junte-as em uma nova tupla.
import tkinter as tk
janela= tk.Tk()
janela.title("tupla 5 letras")
janela.config(background="#2E40EC")
janela.geometry("600x400")
tupla_numero1=(1,2,3,4)
tupla_numero2=(5,6,7,8)
def junta_tupla():
    tupla3=tupla_numero1+tupla_numero2
    label_numero.config(text=f"os numeros juntos sao {tupla3}")



botao_numeros=tk.Button(janela, text="exibir numeros ",command=junta_tupla)
botao_numeros.grid(column=1,row=1,ipady=20)

label_numero=tk.Label(janela,text="")
label_numero.grid(column=2,row=1,pady=30,sticky="n",padx=20)
janela.mainloop()