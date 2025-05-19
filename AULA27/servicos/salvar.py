def salvar_pedido(pedido):
    try:
       with open("pedidos.txt","a",encoding="utf-8") as arq:
           arq.write(str(pedido) + "\n")

    except Exception as e:
        print(f"falha ao  gravar  arquivo {e}")