import tkinter as tk
from tkinter import messagebox
from serviços.insta_pedido import ServicoPedido

class TelaCadastroPedido:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cadastro de Pedido")

       
        self.servico_pedido = ServicoPedido()

        self.valor_label = tk.Label(janela, text="Valor Total:")
        self.valor_label.grid(row=1, column=0)
        self.valor_entry = tk.Entry(janela)
        self.valor_entry.grid(row=1, column=1)

        self.nome_label = tk.Label(janela, text="Nome do Cliente:")
        self.nome_label.grid(row=2, column=0)
        self.nome_entry = tk.Entry(janela)
        self.nome_entry.grid(row=2, column=1)

        self.telefone_label = tk.Label(janela, text="Telefone do Cliente:")
        self.telefone_label.grid(row=3, column=0)
        self.telefone_entry = tk.Entry(janela)
        self.telefone_entry.grid(row=3, column=1)

        self.salvar_button = tk.Button(janela, text="Salvar Pedido", command=self.salvar_pedido)
        self.salvar_button.grid(row=4, column=0, columnspan=2)

    def salvar_pedido(self):
        try:
            nome_cliente = self.nome_entry.get()
            telefone_cliente = self.telefone_entry.get()
            valor_total = float(self.valor_entry.get())

            if not nome_cliente or not telefone_cliente:
                raise ValueError("Nome e telefone do cliente são obrigatórios.")
            self.servico_pedido.criar_pedido(nome_cliente, telefone_cliente, valor_total)

            messagebox.showinfo("Sucesso", "Pedido salvo com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", f"Erro de valor: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o pedido: {e}")
