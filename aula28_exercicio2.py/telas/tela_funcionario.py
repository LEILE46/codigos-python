import tkinter as tk
from tkinter import messagebox
from servicos.criar_funcionario  import ServicoCriarFuncionario
from servicos.salvar  import ServicoSalvarFuncionario

class TelaCadastroFuncionario:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cadastro de Funcionário")
        self.janela.geometry("460x420")
        self.janela.configure(bg="#e8f0fe")

        cor_fundo = "#e8f0fe"
        cor_titulo = "#1a73e8"
        cor_texto = "#202124"
        cor_botao = "#34a853"
        cor_entrada = "#ffffff"

        self.servico_criar_funcionario = ServicoCriarFuncionario()
        self.servico_salvar_funcionario = ServicoSalvarFuncionario()

        tk.Label(self.janela, text="Cadastro de Funcionário", font=("Segoe UI", 16, "bold"),
                 bg=cor_fundo, fg=cor_titulo).grid(row=0, column=0, columnspan=2, pady=20)

        self.nome_entry = self.criar_entrada("Nome do Funcionário:", 1, cor_texto, cor_fundo, cor_entrada)
        self.email_entry = self.criar_entrada("Email:", 2, cor_texto, cor_fundo, cor_entrada)
        self.tipo_entry = self.criar_entrada("Tipo (CLT ou PJ):", 3, cor_texto, cor_fundo, cor_entrada)
        self.cargo_entry = self.criar_entrada("Cargo (se CLT):", 4, cor_texto, cor_fundo, cor_entrada)
        self.cnpj_entry = self.criar_entrada("CNPJ (se PJ):", 5, cor_texto, cor_fundo, cor_entrada)

        tk.Button(self.janela, text="Salvar Funcionário", font=("Segoe UI", 12, "bold"),
                  bg=cor_botao, fg="white", relief="flat", padx=10, pady=6,
                  command=self.salvar_funcionario)\
            .grid(row=6, column=0, columnspan=2, pady=25)

    def criar_entrada(self, texto, linha, cor_texto, cor_fundo, cor_entrada):
        label = tk.Label(self.janela, text=texto, bg=cor_fundo, fg=cor_texto, font=("Segoe UI", 10, "bold"))
        label.grid(row=linha, column=0, sticky="w", padx=15, pady=5)
        entry = tk.Entry(self.janela, font=("Segoe UI", 10), width=30, bg=cor_entrada, relief="solid", bd=1)
        entry.grid(row=linha, column=1, padx=10, pady=5)
        return entry

    def salvar_funcionario(self):
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().strip()
        tipo = self.tipo_entry.get().strip().upper()
        cargo = self.cargo_entry.get().strip()
        cnpj = self.cnpj_entry.get().strip()

        if not nome or not email:
            messagebox.showwarning("Campos obrigatórios", "Nome e Email são obrigatórios.")
            return

        funcionario = self.servico_criar_funcionario.criar_funcionario(
            nome, email, tipo, cargo, cnpj
        )

        if not funcionario:
            messagebox.showwarning("Dados incompletos", "Verifique os campos de acordo com o tipo CLT ou PJ.")
            return

        sucesso = self.servico_salvar_funcionario.salvar_funcionario(funcionario)

        if sucesso:
            messagebox.showinfo("Sucesso", "Funcionário salvo com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Erro ao salvar o funcionário no arquivo.")

    def limpar_campos(self):
        for campo in [self.nome_entry, self.email_entry, self.tipo_entry, self.cargo_entry, self.cnpj_entry]:
            campo.delete(0, tk.END)