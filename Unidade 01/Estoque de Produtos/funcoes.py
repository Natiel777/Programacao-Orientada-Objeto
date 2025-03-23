estoque = {}

def adicionar_produto(nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"Produto '{nome}' adicionado. Quantidade: {estoque[nome]}")

def remover_produto(nome):
    if nome in estoque:
        estoque[nome] = 0
        print(f"Produto '{nome}' removido do estoque.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def atualizar_quantidade(nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"Quantidade do produto '{nome}' atualizada para {quantidade}.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def exibir_estoque():
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("Estoque atual:")
        for nome, quantidade in estoque.items():
            print(f"- {nome}: {quantidade} unidades")
