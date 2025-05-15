import tkinter as tk
from tela.interface import TelaCadastroPedido

def main():
    janela= tk.Tk()
    janela.title("Sistema de Cadastro de Pedidos")
    janela.geometry("400x300")

    def mostrar_tela_pedido():
        TelaCadastroPedido(janela)

    botao_pedido = tk.Button(janela, text="Cadastro de Pedido", command=mostrar_tela_pedido)
    botao_pedido.grid(rowspan=10, column=2)

    janela.mainloop()

if __name__ == "__main__":
    main()
