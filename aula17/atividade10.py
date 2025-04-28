#Desafio: Implemente uma fila com tempo de espera simulado (use time.sleep()) ao atender cada item.
import tkinter as tk
import time
import threading

fila = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

def processar_fila():
    for item in fila:
        status_var.set(f"Atendendo: {item}")
        restante_var.set(f"Itens restantes: {len(fila) - fila.index(item) - 1}")
        time.sleep(2)
    status_var.set("Fila finalizada.")
    restante_var.set("Itens restantes: 0")

def iniciar():
    threading.Thread(target=processar_fila).start()

janela = tk.Tk()
janela.title("Processador de Fila")

status_var = tk.StringVar()
restante_var = tk.StringVar()

tk.Label(janela, text="Fila Genérica", font=("Arial", 16)).pack(pady=10)
tk.Button(janela, text="Iniciar Fila", command=iniciar).pack(pady=10)
tk.Label(janela, textvariable=status_var, font=("Arial", 12)).pack(pady=5)
tk.Label(janela, textvariable=restante_var, font=("Arial", 12)).pack(pady=5)

janela.mainloop()