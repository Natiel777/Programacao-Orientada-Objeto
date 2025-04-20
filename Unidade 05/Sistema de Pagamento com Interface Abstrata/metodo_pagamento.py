from abc import ABC,abstractmethod

class MetodoPagamento(ABC):
	def __init__(self, valor=0.0):
		self.valor = valor

	@abstractmethod	
	def pagar(self):
		pass

class CartaoCredito(MetodoPagamento):
    def pagar(self):
        valor_final = self.valor * 1.05 
        print(f"Pagamento via Cartão de Crédito | Valor original: R${self.valor:.2f} | Valor com acréscimo: R${valor_final:.2f}")

class BoletoBancario(MetodoPagamento):
    def pagar(self):
        valor_final = self.valor * 0.98  
        print(f"Pagamento via Boleto Bancário | Valor original: R${self.valor:.2f} | Valor com desconto: R${valor_final:.2f}")

class Pix(MetodoPagamento):
    def pagar(self):
        print(f"Pagamento via Pix | Valor original: R${self.valor:.2f} | Valor final: R${self.valor:.2f}")
