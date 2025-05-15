def salvar_pedido(pedido):
        try:
            with open("pedidos.txt", "a",encoding='utf-8') as arquivo:
                arquivo.write (str(pedido) + "\n")
            print("Pedido salvo com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar o pedido: {e}")