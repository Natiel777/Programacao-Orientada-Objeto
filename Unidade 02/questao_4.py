class Pessoa:
	def __init__(self, nome, idade, cidade):
		self.nome = nome
		self.idade = idade
		self.cidade = cidade
		
	def apresentar(self):
		print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e moro em {self.cidade}")

pessoa1 = Pessoa("Natiel", 18, "Maranguape")
pessoa2 = Pessoa("João", 20, "Fortaleza")

pessoa1.apresentar()
pessoa2.apresentar()
