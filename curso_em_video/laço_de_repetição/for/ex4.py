"Ler 6 números inteiros e mostrar a soma apenas dos números pares, se o número for impar, desconsidere-o."

num = 0
soma = 0
for i in range(6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos números pares digitados é {soma}')