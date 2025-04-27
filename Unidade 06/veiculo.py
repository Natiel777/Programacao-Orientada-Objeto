class Veiculo:
    total_veiculos = 0  

    def __init__(self, placa="", modelo="", diaria=0.0):
        self.__placa = placa 
        self.modelo = modelo 
        self.diaria = diaria 
        self.__alugado = False 
        Veiculo.total_veiculos += 1 

    def alugar(self):
        if not self.__alugado:
            self.__alugado = True
            print(f"O veículo {self.__placa} foi alugado.")
        else:
            print(f"O veículo {self.__placa} já está alugado.")

    def devolver(self):
        if self.__alugado:
            self.__alugado = False
            print(f"O veículo {self.__placa} foi devolvido e está disponível.")
        else:
            print(f"O veículo {self.__placa} já está disponível.")

    def status(self):
        if self.__alugado:
            print(f"O veículo {self.__placa} está alugado.")
        else:
            print(f"O veículo {self.__placa} está disponível.")

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        print("Erro: a placa não pode ser modificada após o cadastro.")

    @classmethod
    def mostrar_total_veiculos(cls):
        print(f"Total de veículos cadastrados: {cls.total_veiculos}")

    @staticmethod
    def calcular_preco_aluguel(dias, diaria):
        return dias * diaria


        
