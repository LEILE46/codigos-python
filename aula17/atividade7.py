#Permita pesquisar se um item está ou não na fila. Exiba mensagem: “X está na fila” ou “X não encontrado”.
import tkinter as tk
fila_item=["caramelo","pitbull","chowchow"]



def pesquisar_na_fila():
    raça= entrada.get()
    if raça in fila_item:
        resultado_label.config(text=f"raça'{raça}' está na fila.")
    else:
        resultado_label.config(text=f"Tarefa '{raça}' não encontrada na fila.")
    entrada.delete(0, tk.END)
 
janela=tk.Tk()
janela.title("Gerenciador de Filas")
janela.config(background="purple")
janela.geometry("600x400")
 
 
entrada = tk.Entry(janela)
entrada.pack(pady=10)
 
 
pesquisar_button = tk.Button(janela, text="Pesquisar Tarefa na Fila", command=pesquisar_na_fila)
pesquisar_button.pack(pady=5)
 
 
resultado_label = tk.Label(janela, text="", bg="purple")
resultado_label.pack(pady=20)
 
 
janela.mainloop()