compras = [ 
    ["Ana", 150.75],
    ["Bruno", 520.00],
    ["Carla", 95.50],
    ["Daniel", 890.99],
    ["Elisa", 320.00]
]

maior = -1
menor = 99999999

dict_clientes = dict()

for clientes in compras:

    cliente_maior = list()
    cliente_menor = list()
    nome = clientes[0]
    valor = clientes[1]

    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor

cliente_maior = list(, maior)
print(cliente_maior)


