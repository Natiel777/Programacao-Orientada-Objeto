class Restaurante:
    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha

    def descrever_restaurante(self):
        print(f"O restaurante {self.nome_restaurante} serve comida {self.tipo_cozinha}")

    def abrir_restaurante(self):
        print(f"O restaurante {self.nome_restaurante} está aberto!")

    def __str__(self):
        return (f"O restaurante {self.nome_restaurante} serve comida {self.tipo_cozinha}")

restaurante1 = Restaurante("Cabana", "Brasileira")
restaurante2 = Restaurante("Al Nono Luigi", "Italiana")
restaurante3 = Restaurante("Yumi", "Japonesa")

print("Usando o método descrever restaurante:")
restaurante1.descrever_restaurante()
restaurante1.descrever_restaurante()
restaurante1.descrever_restaurante()

print("Usando o método __str__:")
print(restaurante1)
print(restaurante2)
print(restaurante3)
