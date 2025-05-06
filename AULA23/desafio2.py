cardapio={"1)arroz e feijao":20.00,
          "2)lasanha":15.00,
          "3)churrasco com arroz":30.00,
          "4)macarrao":18.00,
          "5)strogonoff":25.00}
print(cardapio)
usuario=input("digite o numero do  prato que deseja :")
if usuario == "1":
    valor=cardapio["1)arroz e feijao"]
    print(f"este prato custa {valor}")
elif usuario =="2":
    valor=cardapio["2)lasanha"]
    print(f"este prato custa {valor}")
elif usuario =="3":
    valor=cardapio["3)churrasco com arroz"]
    print(f"este prato custa {valor}")
elif usuario =="4":
    valor=cardapio["4)macarrao"]
    print(f"este prato custa {valor}")
elif usuario =="5":
    valor=cardapio["5)strogonoff"]
    print(f"este prato custa {valor}")
else:
    print("adicione uma das opiçao acima")