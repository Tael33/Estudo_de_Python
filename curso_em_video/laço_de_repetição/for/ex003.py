'''Soma dos números impares de 1 a 500'''
soma = 0
for num in range(1,501,2):
    if num % 3 == 0:
        soma += num
print(f'A soma dos números impares de 1 a 500 é {soma}')