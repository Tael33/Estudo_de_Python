# crie um progra de leia o nome de uma cidade e diga se ela começa com ou não coma o nome "santo"


cidd = input('Digite um nome de uma cidade: ').upper().strip()

print(cidd[:5] == 'SANTO')
