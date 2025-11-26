# Escrava um programa para aprovar o ampréstimo bancário para a
# compra de uma casa. Pargunta o valor da casa, o salário do comprador
# a em quantos anos ala vai pagar.
# A prestaSao mensal. nao pode excader 30% do salario ou antao o
# ampréstimo sará nagado.

casa = float(input('Valor da casa R$'))
salario = float(input('Salário do comprador R$'))
anos = int(input('Quantos anos de financiamento? '))

prestaçao = casa / (anos * 12)

if prestaçao <= salario * 0.3:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')