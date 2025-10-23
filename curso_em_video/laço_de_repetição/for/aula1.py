'''for fala in range(0, 6):
    print(f'OI, EU TE ESCUTEI {fala+1} VEZES')
print('FIM')

for fala in range(6, 0, -1):
    print(f'OI, EU TE ESCUTEI {fala} VEZES')
print('FIM')

for fala in range(0, 7, 2):
    print(f'OI, EU TE ESCUTEI {fala} VEZES')
print('FIM')

for fala in range(1, 6, 2):
    print(f'OI, EU TE ESCUTEI {fala+1} VEZES')
print('FIM')

n = int(input('Digite um número: '))
for fala in range(0, n+1):
    print(f'OI, EU TE ESCUTEI {fala} VEZES')
print('FIM')

n = int(input('Digite um número: '))
for fala in range(0, n):
    print(f'OI, EU TE ESCUTEI {fala+1} VEZES')
print('FIM')'''

inicio = int(input('Digite o Início: '))
fim = int(input('Digite o Fim: '))
passo = int(input('Digite o Passo: '))

for fala in range(inicio, fim+1, passo):
    print(f'OI, EU TE ESCUTEI {fala} VEZES')
print('FIM')

for fala in range(inicio, fim, passo):
    print(f'OI, EU TE ESCUTEI {fala+1} VEZES')
print('FIM')

for fala in range(inicio, fim, passo):
    print(f'OI, EU TE ESCUTEI {fala} VEZES')
print('FIM')