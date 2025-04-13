from conta_corrente import ContaCorrente
from datetime import datetime as dt

class ContaEspecial(ContaCorrente):
    def __init__(self, usuario, data_abertura=dt(1900, 1, 1), saldo=0.0, taxa_manutencao=10.0, limite=500.0):
        super().__init__(usuario, data_abertura, saldo, taxa_manutencao)
        self.limite = limite  

    def consultarSaldo(self):
        return self.saldo + self.limite
    
    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor

    def transferir(self, outra_conta, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            outra_conta.saldo += valor
            
    def alterar_limite(self, novo_limite):
        self.limite = novo_limite
