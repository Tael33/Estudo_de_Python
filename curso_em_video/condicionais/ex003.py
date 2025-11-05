# Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar.

num = int(input('Digite um número inteiro para descobrir se é par ou ímpar: '))

if num % 2 == 0:
    print(f'{num} é par!')
else:
    print(f'{num} é ímpar!')