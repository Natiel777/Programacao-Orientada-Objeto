class Carro: 
    def __init__(self, marca, modelo, ano, cor):  
        self.marca = marca  
        self.modelo = modelo  
        self.ano = ano  
        self.cor = cor   

carro1 = Carro("Toyota", "Supra", 1993, "Preto")  
carro2 = Carro("Honda", "Civic", 1992, "Vermelho")  

print(carro1.marca, carro1.modelo, carro1.ano, carro1.cor)
print(carro2.marca, carro2.modelo, carro2.ano, carro2.cor)
