#Crie uma fila com 5 nomes. Mostre a fila e depois remova o primeiro nome (simulando atendimento).
import tkinter as tk

fila_atendimento=["leileane","erica","vinicios","eric","gaby"]

def mostrar_fila():
    lista_fila.delete(0, tk.END)  
    for nome in fila_atendimento:
        lista_fila.insert(tk.END, nome)  

def atender_cliente():
    if fila_atendimento:
        fila_atendimento.pop(0)  
    mostrar_fila()  

janela = tk.Tk()
janela.title("Fila de Atendimento")

tk.Label(janela, text="Fila de Atendimento", font=("Arial", 16)).pack(pady=10)

lista_fila = tk.Listbox(janela, height=6, width=30, font=("Arial", 12))
lista_fila.pack(pady=10)


botao_atender = tk.Button(janela, text="Atender Cliente", font=("Arial", 12), command=atender_cliente)
botao_atender.pack(pady=10)

mostrar_fila()
janela.mainloop()




