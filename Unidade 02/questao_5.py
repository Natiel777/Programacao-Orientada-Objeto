class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):    
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco

livro1 = Livro("Harry Potter", "J.K. Rowling", 1997, 30)
livro2 = Livro("O Príncipe", "Nicolau Maquiavel", 1532, 20)

print(f"Título: {livro1.titulo}, Autor: {livro1.autor}, Ano: {livro1.ano_publicacao}, Preço: R${livro1.preco}")
print(f"Título: {livro2.titulo}, Autor: {livro2.autor}, Ano: {livro2.ano_publicacao}, Preço: R${livro2.preco}")
