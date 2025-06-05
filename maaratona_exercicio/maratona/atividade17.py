agenda = {}
continuar = True
 
while continuar:
    print("\n1 - Adicionar\n2 - Listar\n3 - Buscar\n4 - Remover\n5 - Sair")
    opcao = input("Escolha: ")
 
    if opcao == '1':
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
 
    elif opcao == '2':
        for nome in agenda:
            print(nome + ": " + agenda[nome])
 
    elif opcao == '3':
        nome = input("Buscar nome: ")
        if nome in agenda:
            print(agenda[nome])
        else:
            print("Contato não encontrado.")
 
    elif opcao == '4':
        nome = input("Nome a remover: ")
        if nome in agenda:
            del agenda[nome]
            print("Contato removido.")
        else:
            print("Contato não encontrado.")
 
    elif opcao == '5':
        continuar = False
 
    else:
        print("Opção inválida.")