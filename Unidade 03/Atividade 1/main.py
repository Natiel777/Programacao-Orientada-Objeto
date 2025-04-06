from datetime import datetime as dt
from usuario import Usuario
from conta import Conta

usuario1 = Usuario()

rg = int(input("Digite seu RG: "))
cpf = int(input("Digite seu CPF: "))
nome = input("Digite seu nome: ")
dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

usuario1.set_rg(rg)
usuario1.set_cpf(cpf)
usuario1.set_nome(nome)
usuario1.set_data_nascimento(dia, mes, ano)

conta1 = Conta(usuario1, dt(2025, 4, 5), 1000)

print("- Informações da Conta -")
print(f"Agência: {conta1.get_agencia()}")
print(f"Data de abertura: {conta1.get_data_abertura().strftime('%d/%m/%Y')}")
print(f"Saldo: R${conta1.get_saldo():.2f}")

print("- Informações do Usuário -")
print(f"RG: {usuario1.get_rg()}")
print(f"CPF: {usuario1.get_cpf()}")
print(f"Nome: {usuario1.get_nome()}")
print(f"Data de nascimento: {usuario1.get_data_nascimento().strftime('%d/%m/%Y')}")
