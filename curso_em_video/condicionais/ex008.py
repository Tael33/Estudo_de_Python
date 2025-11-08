# desenvolva un programa que leia o comprimento de três retas e diga ao usuário
# se ela pode formar um triâgulo.

print('Analisador de triângulo!')

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')