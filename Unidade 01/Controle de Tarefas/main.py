from funcoes import adicionar_tarefa, marcar_como_concluida, listar_tarefas

lista_tarefas = []

while True:
    print("\n- Gerenciador de Tarefas -")
    print("1. Adicionar Tarefa")
    print("2. Marcar Tarefa como Concluída")
    print("3. Mostrar Tarefas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(lista_tarefas, titulo, descricao)

    elif opcao == "2":
        titulo = input("Digite o título da tarefa que deseja marcar como concluída: ")
        marcar_como_concluida(lista_tarefas, titulo)

    elif opcao == "3":
        listar_tarefas(lista_tarefas)

    elif opcao == "4":
        print("Saindo do gerenciador...")
        break

    else:
        print("Opção inválida. Tente novamente outra.")


