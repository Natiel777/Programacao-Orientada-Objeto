from conta import Conta
from datetime import datetime as dt

class ContaCorrente(Conta):
    def __init__(self, usuario, data_abertura=dt(1900, 1, 1), saldo=0.0, taxa_manutencao=10.0):
        super().__init__(usuario, data_abertura, saldo)
        self.taxa_manutencao = taxa_manutencao

    def cobrar_manutencao(self):
        if self.saldo >= self.taxa_manutencao:
            self.saldo -= self.taxa_manutencao
            
    def alterar_taxa_manutencao(self, nova_taxa):
        self.taxa_manutencao = nova_taxa
