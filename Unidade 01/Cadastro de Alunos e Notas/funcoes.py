def adicionar_aluno(alunos, nome, notas):
    if nome not in alunos:
        alunos[nome] = notas
        print(f"Aluno {nome} adicionado com sucesso.")
    else:
       print("Aluno já cadastrado.")
       
def remover_aluno(alunos, nome):
    if nome in alunos:
        alunos[nome] = 0
        print(f"Aluno {nome} removido com sucesso.")
    else:
        print("Aluno não encontrado.")

def atualizar_notas(alunos, nome, notas):
    if nome in alunos:
        alunos[nome] = notas
        print(f"Notas do aluno {nome} atualizadas com sucesso.")
    else:
        print("Aluno não encontrado.")

def mostrar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for nome, notas in alunos.items():
            print(f"{nome}: {notas}")

def calcular_media(alunos, nome):
    if nome in alunos:
        media = sum(alunos[nome]) / len(alunos[nome])
        print(f"Média do aluno {nome}: {media:.2f}")
    else:
        print("Aluno não encontrado.")
