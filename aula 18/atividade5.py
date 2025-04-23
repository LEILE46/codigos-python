#Crie uma tupla com 4 números. Exiba a soma dos valores.
import tkinter as tk
janela= tk.Tk()
janela.title("tupla numero")
janela.config(background="#2E40EC")
janela.geometry("600x400")
tupla_numero=(2,2,1,3)
soma=0

def soma_numeros():
    global soma 
    for numero in tupla_numero:
        soma+= numero  
    label_numeros.config(text=soma)
    botao_numeros.config(state="disabled")




botao_numeros = tk.Button(janela, text="exiba soma ",command=soma_numeros)
botao_numeros.pack(side="top")

label_numeros=tk.Label(janela,text="")
label_numeros.pack(side="top",pady=30,anchor="s")
janela.mainloop()
