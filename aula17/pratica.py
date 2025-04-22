fila=[]#criando lista

while True:#laço de repetiçao 
    print("\n1- adicionar cliente")
    print("2-atender cliente")
    print("3- ver fila ")
    print("4-sair ")

    opçao = input ("escolha uma opçao :")#variavel

    if opçao =="1":
        nome=input ("nome cliente:")
        fila.append(nome)
        print(f"{nome} entrou na fila ")
    elif opçao == "2":
        if fila:
            atendido= fila.pop(0)
            print (f"{atendido} foi atendido.")
        else:
            print ("fila vazia!")
    elif opçao == "3":
        print("Fila atual:", fila)
 
    elif opçao == "4":
 
     break
 
    else:
 
        print("Opção inválida.")