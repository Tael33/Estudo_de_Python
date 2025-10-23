'''Crie um programa que leio um número Real qualquer pelo teclodo e
mostre na tela o sua portao Inteiro.'''

'''from math import trunc
num = float(input('Digite um número real pra reseber o número no forma inteira: '))

print(f"O valor digitados foi {num} e sua porção inteira é {trunc(num)}")
print(f"O valor digitados foi {num} e sua porção inteira é {int(num)}")'''


'''Foro um programa qua leia o comprimento do coteto oposto e do coteto
adjacente de um triânquio retângulo. colcule ce mostre o comprimento
do hipotenusa.'''

# Posibelidade 1
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjecente = float(input('Digite o valor do cateto adjecente: '))

hipotenusa = (cateto_oposto ** 2 + cateto_adjecente ** 2)** (1/2)
print(f'A hipotenusa tem o comprimento de {hipotenusa:.2f}')

# Posibilidade 2
import math
cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjecente = float(input('Digite o valor do cateto adjecente: '))
hipot = math.hypot(cat_oposto, cat_adjecente)
print(f'A hipotenusa tem o comprimento de {hipot:.2f}')
    
