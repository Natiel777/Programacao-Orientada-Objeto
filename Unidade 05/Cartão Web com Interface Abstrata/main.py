from cartao_web import DiaDosNamorados, Natal, Aniversario
		
cartao1 = DiaDosNamorados("Clare")
cartao2 = Natal("Natiel")
cartao3 = Aniversario("Messi")

cartao1.show_message()
cartao2.show_message()
cartao3.show_message()


"""Polimorfismo acontece no código quando a variável cartao, que é do tipo CartaoWeb, 
é usada para armazenar objetos de diferentes subclasses (DiaDosNamorados, Natal e Aniversario).
Mesmo usando o mesmo método show_message(), o comportamento muda conforme a classe do objeto,
exibindo mensagens diferentes para cada tipo de cartão."""
