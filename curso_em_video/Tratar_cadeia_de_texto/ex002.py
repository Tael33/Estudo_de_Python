# faça um programa que leia um número de 0 a 9999 e mostre
# cada um dos digitos separados

num = int(input('Digitr um número de 0 a 9999: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'Analisando o número {num} ...')
print(f' Milhar: {milhar}\n Centena: {centena}\n Dezena: {dezena}\n Unidade: {unidade}')

