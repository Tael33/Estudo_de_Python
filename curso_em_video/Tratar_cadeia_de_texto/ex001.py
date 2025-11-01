nome = input('Qual o seu nome completo: ')

print(nome.title())

print(nome.upper())

print(nome.lower())

Nome = nome.strip().split()
nomeJ = ''.join(Nome)
print(len(nomeJ))

print(len(Nome[0]))