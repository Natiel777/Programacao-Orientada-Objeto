from funcoes import adicionar_aluno, remover_aluno, atualizar_notas, mostrar_alunos, calcular_media

alunos = {}

while True:
    print("\n- Sistema de Gerenciamento de Alunos e Notas - ")
    print("1. Adicionar aluno e suas notas")
    print("2. Remover aluno")
    print("3. Atualizar as notas de um aluno")
    print("4. Mostrar todos os alunos com suas notas")
    print("5. Calcular média de um aluno")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        notas = [
            float(input("Digite a Nota 01 do aluno: ")),
            float(input("Digite a Nota 02 do aluno: ")),
            float(input("Digite a Nota 03 do aluno: ")),
            float(input("Digite a Nota 04 do aluno: "))
        ]
        adicionar_aluno(alunos, nome, notas)

    elif opcao == "2":
        nome = input("Digite o nome do aluno a ser removido: ")
        remover_aluno(alunos, nome)

    elif opcao == "3":
        nome = input("Digite o nome do aluno: ")
        notas = [
            float(input("Digite a nova Nota 01 do aluno: ")),
            float(input("Digite a nova Nota 02 do aluno: ")),
            float(input("Digite a nova Nota 03 do aluno: ")),
            float(input("Digite a nova Nota 04 do aluno: "))
        ]
        atualizar_notas(alunos, nome, notas)

    elif opcao == "4":
        mostrar_alunos(alunos)

    elif opcao == "5":
        nome = input("Digite o nome do aluno para calcular a média: ")
        calcular_media(alunos, nome)

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente outra.")
