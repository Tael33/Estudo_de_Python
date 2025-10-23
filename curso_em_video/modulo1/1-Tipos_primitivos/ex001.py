'''num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
print(f'A soma entre {num1} e {num2} é igual a {soma}')'''

valor = input('Digite um valor: ')
print(f'O tipo primitivo de {valor} é {type(valor)}')
print(f'Só tem espaços? {valor.isspace}')
print(f'É um número? {valor.isnumeric()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É alfanúmerico? {valor.isalnum()}')
print(f'É tudo maiúscula? {valor.isupper()}')
print(f'É tudo menúsculo? {valor.islower()}')
print(f'É capitalizada "Maiúculas e menúsculas"? {valor.istitle()}')