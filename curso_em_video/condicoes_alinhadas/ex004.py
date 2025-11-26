# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao
# serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o
# tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Ano de nascimento: '))

atual = date.today().year

idade = atual - ano

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    exedido = idade - 18
    print(f'Você já deveria ter se alistado há {exedido} anos.')
else:
    falta = 18 - idade
    print(f'Ainda faltam {falta} anos para o alistamento.')

