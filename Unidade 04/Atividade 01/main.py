from datetime import datetime as dt
from usuario import Usuario
from conta import Conta
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente
from conta_especial import ContaEspecial

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

poupanca = ContaPoupanca(usuario1, dt(2025, 4, 1), 3000, 0.02)
corrente = ContaCorrente(usuario1, dt(2025, 4, 1), 500)
especial = ContaEspecial(usuario1, dt(2025, 4, 1), 300, limite=1000)

print("- Conta Poupança -")
print(f"Saldo atual: R${poupanca.get_saldo():.2f}")
poupanca.aplicar_juros()
print(f"Saldo após juros: R${poupanca.get_saldo():.2f}")
print(f"Simulação de 6 meses: R${poupanca.simular_rendimento(6):.2f}")

print("- Conta Corrente -")
print(f"Saldo atual: R${corrente.get_saldo():.2f}")
corrente.cobrar_manutencao()
print(f"Saldo após manutenção: R${corrente.get_saldo():.2f}")
corrente.alterar_taxa_manutencao(5)
print("Nova taxa de manutenção definida: R$5.00")

print("- Conta Especial -")
print(f"Saldo disponível (com limite): R${especial.consultarSaldo():.2f}")
especial.sacar(4000)
print(f"Saldo após saque de R$1000: R${especial.get_saldo():.2f}")
especial.alterar_limite(1500)
print(f"Novo limite definido: R${especial.limit
e:.2f}")

