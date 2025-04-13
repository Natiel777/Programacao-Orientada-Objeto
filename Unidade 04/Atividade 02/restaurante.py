class Restaurante:
    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
        self.numeros_servidos = 0

    def descrever_restaurante(self):
        print(f"O restaurante {self.nome_restaurante} serve comida {self.tipo_cozinha}")

    def abrir_restaurante(self):
        print(f"O restaurante {self.nome_restaurante} está aberto!")
        
    def getnumero_servidos(self):
        return self.numeros_servidos

    def setnumero_servidos(self, novo_valor):
        if novo_valor >= 0:
            self.numeros_servidos = novo_valor
              
    def incremente_numero_servidos(self, incremento):
        if incremento > 0:
            total = self.getnumero_servidos() + incremento
            self.setnumero_servidos(total)

    def __str__(self):
        return (f"O restaurante {self.nome_restaurante} serve comida {self.tipo_cozinha}")

restaurante1 = Restaurante("Cabana", "Brasileira")
restaurante2 = Restaurante("Al Nono Luigi", "Italiana")
restaurante3 = Restaurante("Yumi", "Japonesa")
restaurante = Restaurante("La Sabor", "Mexicana")

print("- Usando o método descrever restaurante -")
restaurante1.descrever_restaurante()
restaurante1.descrever_restaurante()
restaurante1.descrever_restaurante()

print("- Usando o método __str__ -")
print(restaurante1)
print(restaurante2)
print(restaurante3)

print("- Mostrando o número de clientes atual e atualizado - ")
print(f"Número de clientes atendidos: {restaurante.numeros_servidos}")

restaurante.numeros_servidos = 50

print(f"Número de clientes atendidos atualizado: {restaurante.numeros_servidos}")

print("- Mostrando o número de clientes atual e atualizado usando get e set -")
print(f"Número de clientes atendidos: {restaurante.getnumero_servidos()}")

restaurante.setnumero_servidos(100)
print(f"Número de clientes atendidos atualizado: {restaurante.getnumero_servidos()}")

print("- Mostrando o número de clientes com incremento -")
restaurante.incremente_numero_servidos(30)

print(f"Número de clientes atendidos atualizado: {restaurante.getnumero_servidos()}")

