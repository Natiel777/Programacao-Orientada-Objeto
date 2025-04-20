from metodo_pagamento import CartaoCredito, BoletoBancario, Pix

valor = float(input("Valor da compra: "))
metodo = input("Método de pagamento (cartao, boleto, pix): ").strip().lower()

if metodo == "cartao":
    pagamento = CartaoCredito(valor)
elif metodo == "boleto":
    pagamento = BoletoBancario(valor)
elif metodo == "pix":
    pagamento = Pix(valor)
else:
    print("Método inválido. Digite um dos métodos citados.")
    
pagamento.pagar()

"""O polimorfismo facilitou a implementação do sistema de pagamento porque permite que cada método de pagamento (como Cartão de Crédito, Boleto e Pix) tenha sua própria implementação do método pagar(), 
sem que o código que utiliza esses métodos precise saber como cada pagamento é processado. Isso melhora a flexibilidade e a extensibilidade do sistema.

As vantagens de utilizar uma classe abstrata (funcionando como uma interface) são:

Uniformidade: Garante que todos os métodos de pagamento implementem o método pagar(), tornando o sistema mais consistente.

Desacoplamento: O código que lida com pagamentos não precisa saber os detalhes de cada tipo de pagamento, tornando o sistema mais fácil de modificar e expandir.

Escalabilidade: Novos métodos de pagamento podem ser adicionados sem modificar o código existente, apenas criando novas classes que implementem a interfa
ce."""
