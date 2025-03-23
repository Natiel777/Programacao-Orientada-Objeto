from funcoes import adicionar_produto, remover_produto, atualizar_quantidade, exibir_estoque

while True:
    print("\n- Sistema de Gerenciamento de Estoque da Loja -")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Atualizar quantidade de um produto")
    print("4. Mostrar estoque")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade do produto: "))
        adicionar_produto(nome, quantidade)
    elif opcao == "2":
        nome = input("Nome do produto a ser removido: ")
        remover_produto(nome)
    elif opcao == "3":
        nome = input("Nome do produto: ")
        quantidade = int(input("Nova quantidade: "))
        atualizar_quantidade(nome, quantidade)
    elif opcao == "4":
        exibir_estoque()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente outra.")
