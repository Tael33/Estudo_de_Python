# Faça um programa que leia um ano qulquer e verifique se ele é um ano bissexto.

from datetime import date

def verificar_bissexto(ano):
    
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

ano = int(input('Digete um ano para saber se ele é um ano bissexto ou não, OU 0 para o ano atual:  '))

if ano == 0:
    ano = date.today().year

if verificar_bissexto(ano) == True:
    print(f'O ano {ano} é Bissexto!')
else:
    print(f'O ano {ano} não é Bissexto!')

