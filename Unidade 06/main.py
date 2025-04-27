from veiculo import Veiculo
veiculo1 = Veiculo("ABC-1234", "Civic", 150.0)
veiculo2 = Veiculo("XYZ-5678", "Corolla", 180.0)

print("\n- Alugando veículo 1 -")
veiculo1.alugar()
veiculo1.status()

print("\n- Devolvendo veículo 1 -")
veiculo1.devolver()
veiculo1.status()

print("\n- Verificando encapsulamento da placa -")
print(f"Placa do veículo 1: {veiculo1.placa}")
veiculo1.placa = "DEF0000"  

print("\n- Total de veículos cadastrados -")
Veiculo.mostrar_total_veiculos()

print("\n- Calculando valor do aluguel -")
dias = 7
valor = Veiculo.calcular_preco_aluguel(dias, veiculo2.diaria)
print(f"Valor do aluguel do {veiculo2.modelo} por {dias} dias: R${valor:.2f}")
