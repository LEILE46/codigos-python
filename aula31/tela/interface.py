import tkinter as tk
from tkinter import messagebox
from servicos.servico_login import ServicoLogin
from servicos.servico_fatura import ServicoFatura

class Interface:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cálculo de Fatura Águas Guariroba")
        self.janela.geometry("400x400") 
        self.janela.config(bg="#01FDDB")  
        self.servico_login = ServicoLogin()
        self.servico_fatura = ServicoFatura()
   
        self.criar_widgets()
    
    def criar_widgets(self):
        self.login_frame = tk.Frame(self.janela, bg="#01FDDB")
        self.login_frame.grid(row=0, column=0, padx=20, pady=30)

        self.senha_label = tk.Label(self.login_frame, text="Senha:", font=("Arial", 14), bg="#f0f0f0")
        self.senha_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.senha_entry = tk.Entry(self.login_frame, show="*", font=("Arial", 14), width=20)
        self.senha_entry.grid(row=0, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self.login_frame, text="Login", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.realizar_login)
        self.login_button.grid(row=1, columnspan=2, pady=20)

    def realizar_login(self):
        senha_digitada = self.senha_entry.get()
        if self.servico_login.autenticar(senha_digitada):
            self.login_frame.grid_forget() 
            self.show_consumo_frame()  
        else:
            messagebox.showerror("Erro", "Senha incorreta! Acesso negado.")
    
    def show_consumo_frame(self):
    
        self.consumo_frame = tk.Frame(self.janela, bg="#01FDDB")
        self.consumo_frame.grid(row=1, column=0, padx=20, pady=30)

        self.consumo_label = tk.Label(self.consumo_frame, text="Consumo de água (m³):", font=("Arial", 14), bg="#f0f0f0")
        self.consumo_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.consumo_entry = tk.Entry(self.consumo_frame, font=("Arial", 14), width=20)
        self.consumo_entry.grid(row=0, column=1, padx=10, pady=10)

        self.calcular_button = tk.Button(self.consumo_frame, text="Calcular Fatura", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.calcular_fatura)
        self.calcular_button.grid(row=1, columnspan=2, pady=20)
    
    def calcular_fatura(self):
        try:
            consumo = float(self.consumo_entry.get())
            fatura = self.servico_fatura.calcular_fatura(consumo)
            self.exibir_fatura(fatura)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o consumo.")
    
    def exibir_fatura(self, fatura):
        self.resultado_frame = tk.Frame(self.janela, bg="#f0f0f0")
        self.resultado_frame.grid(row=2, column=0, padx=20, pady=30)

        valor_agua_label = tk.Label(self.resultado_frame, text=f"Valor da Água: R$ {fatura.valor_agua}", font=("Arial", 14), bg="#f0f0f0")
        valor_agua_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        valor_esgoto_label = tk.Label(self.resultado_frame, text=f"Valor do Esgoto: R$ {fatura.valor_esgoto:2f}", font=("Arial", 14), bg="#f0f0f0")
        valor_esgoto_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        valor_total_label = tk.Label(self.resultado_frame, text=f"Valor Total da Fatura: R$ {fatura.valor_total:2f}", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#4CAF50")
        valor_total_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

if __name__ == "__main__":
    janela = tk.Tk()
    interface = Interface(janela)
    janela.mainloop()