def adicionar_tarefa(lista_tarefas, titulo, descricao):
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }
    lista_tarefas.append(tarefa)
    print(f"Tarefa \"{titulo}\" adicionada!")

def marcar_como_concluida(lista_tarefas, titulo):
    for tarefa in lista_tarefas:
        if tarefa["titulo"] == titulo:
            tarefa["status"] = "Concluído"
            print(f"Tarefa \"{titulo}\" concluída!")
            return
    print(f"Tarefa \"{titulo}\" não encontrada.")

def listar_tarefas(lista_tarefas):
    print("\n- Tarefas Pendentes -")
    for tarefa in lista_tarefas:
        if tarefa["status"] == "Pendente":
            print(f"Título: {tarefa['titulo']}")
            print(f"Descrição: {tarefa['descricao']}")
            print("Status: Pendente\n")

    print("- Tarefas Concluídas -")
    for tarefa in lista_tarefas:
        if tarefa["status"] == "Concluído":
            print(f"Título: {tarefa['titulo']}")
            print(f"Descrição: {tarefa['descricao']}")
            print("Status: Concluído\n")
