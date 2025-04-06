from datetime import datetime as dt
from usuario import Usuario  
import random

class Conta:   
    def __init__(self, usuario, data_abertura=dt(1900, 1, 1), saldo=0.0):
        self.agencia = random.randint(0, 999)
        self.usuario = usuario
        self.data_abertura = data_abertura
        self.saldo = saldo
	
    def get_agencia(self):
        return self.agencia
    
    def set_agencia(self, agencia):
        self.agencia = agencia
    
    def get_usuario(self):
        return self.usuario
    
    def set_usuario(self, usuario):
        self.usuario = usuario
        
    def get_data_abertura(self):
        return self.data_abertura
    
    def set_data_abertura(self, dia, mes, ano):
        self.data_abertura = dt(ano, mes, dia)
        
    def get_saldo(self):
        return self.saldo
    
    def set_saldo(self, saldo):
        self.saldo = saldo
        
    def __str__(self):
        return (f"Agência: {self.agencia}\n"
                f"Usuário: {self.usuario}\n"
                f"Data de abertura: {self.data_abertura.strftime('%d/%m/%Y')}\n"
                f"Saldo: R${self.saldo:.2f}")
