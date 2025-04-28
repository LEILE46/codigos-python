#Crie uma fila de embarque. Ao chamar passageiros, mostre quem foi chamado e quantos restam na fila.
import tkinter as tk

fila_embarque = ["Ana", "Bruno", "Carla", "Diego", "Eduarda"]

def chamar_passageiro():
    if fila_embarque:
        passageiro = fila_embarque.pop(0)  # Remove o primeiro da lista
        resultado_var.set(f"Passageiro chamado: {passageiro}")
        restante_var.set(f"Passageiros restantes: {len(fila_embarque)}")
    else:
        resultado_var.set("Todos os passageiros foram chamados.")
        restante_var.set("Passageiros restantes: 0")

janela = tk.Tk()
janela.title("Fila de Embarque")

resultado_var = tk.StringVar()
restante_var = tk.StringVar()


tk.Label(janela, text="Fila de Embarque", font=("Arial", 16)).pack(pady=10)
tk.Button(janela, text="Chamar próximo passageiro", command=chamar_passageiro).pack(pady=10)
tk.Label(janela, textvariable=resultado_var, font=("Arial", 12)).pack(pady=5)
tk.Label(janela, textvariable=restante_var, font=("Arial", 12)).pack(pady=5)


janela.mainloop()