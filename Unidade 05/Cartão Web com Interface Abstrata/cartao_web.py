from abc import ABC,abstractmethod

class CartaoWeb(ABC):
	def __init__(self, destinatario="ind"):
		self.destinatario = destinatario

	@abstractmethod
	def show_message(self):
		pass	

class DiaDosNamorados(CartaoWeb):
	def __init__(self, destinatario="ind"):	
		super().__init__(destinatario)
	
	def show_message(self):
		print(f"Feliz Dia dos Namorados! {self.destinatario}")
	
class Natal(CartaoWeb):
	def __init__(self, destinatario="ind"):	
		super().__init__(destinatario)
	
	def show_message(self):
		print(f"Feliz Natal! {self.destinatario}")
	
class Aniversario(CartaoWeb):
	def __init__(self, destinatario="ind"):	
		super().__init__(destinatario)
	
	def show_message(self):
		print(f"Feliz Aniversário! {self.destinatario}")
		
