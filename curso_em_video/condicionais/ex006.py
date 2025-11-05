# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.



nums = list()
for _ in range(3):
    num = float(input(f'Digete o {_+1}º número: '))
    nums.append(num)

maior = -1
menor = 9999999999

for num in nums:
    if num > maior:
        maior = num
    else:
        menor = num
print(f'O maior é {maior} e o menor é {menor}')