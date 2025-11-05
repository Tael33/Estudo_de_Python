# Escreva um programa que faça o computador "pensar" em um 
# número inteiro entre 0 e 5 e peça para o usuário tentar 
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu 
# ou perdeu 

from random import randint
from time import sleep

numM = randint(0,5)

print('-=' * 20)
print('Eu estou pensando em número entre 0 e 5!\nTenta adivinhar!')
print('-=' * 20)

numU = int(input('Escolha o seu número de 0 a 5: '))

print('PROCESSANDO...')
sleep(3)

if numU == numM:
    print('Você conseguiu me vencer!')
else:
    print(f'O número foi {numM}, por tanto, Você perdeu!')