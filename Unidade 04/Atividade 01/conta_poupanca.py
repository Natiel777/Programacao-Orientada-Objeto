from conta import Conta
from datetime import datetime as dt

class ContaPoupanca(Conta):
    def __init__(self, usuario, data_abertura=dt(1900, 1, 1), saldo=0.0, taxa_juros=0.01):
        super().__init__(usuario, data_abertura, saldo)
        self.taxa_juros = taxa_juros  

    def aplicar_juros(self):
        self.saldo += self.saldo * self.taxa_juros
    
    def simular_rendimento(self, meses):
        saldo_simulado = self.saldo
        for i in range(meses):
            saldo_simulado += saldo_simulado * self.taxa_juros
        return saldo_simulado
