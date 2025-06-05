import tkinter as tk
from servicos.fatura import calcular_fatura

def tela_principal(nome_usuario):
    def calcular():
        try:
            consumo = float(entry_consumo.get())  
        
            valor_agua, valor_esgoto, valor_total = calcular_fatura(consumo)
          
            label_resultado.config(text=f"Água: R$ {valor_agua:.2f}\nEsgoto: R$ {valor_esgoto:.2f}\nTotal: R$ {valor_total:.2f}")
        except ValueError:
            label_resultado.config(text="Entrada inválida! Por favor, insira um número válido.")

    root = tk.Tk()
    root.title(f"Águas Guariroba - {nome_usuario}")

    root.config(bg="#2196F3")  

    tk.Label(root, text=f"Bem-vindo, {nome_usuario}!", fg="white", bg="#2196F3", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Informe o consumo (em m³):", fg="white", bg="#2196F3", font=("Arial", 12)).pack(pady=10)
    entry_consumo = tk.Entry(root, font=("Arial", 12))
    entry_consumo.pack(pady=5)

    tk.Button(root, text="Calcular", bg="#4CAF50", fg="white", font=("Arial", 12), command=calcular).pack(pady=20)

    label_resultado = tk.Label(root, text="Resultado da fatura aparecerá aqui.", fg="white", bg="#2196F3", font=("Arial", 12))
    label_resultado.pack(pady=20)

    root.mainloop()