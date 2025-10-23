'''dados1 = list()
dados1.append('Pedro') # dados1[0]
dados1.append(25) # dados1[1]

dados2 = list()
dados2.append('Maria') # dados2[0]
dados2.append(19) # dados2[1]


pessaos = list()
# [: ] Isso faz uma cooia dos elementos. Faz um fatiamento completo da lista "dados" ou seja pega todos os elementos da lista.
pessoas.append(dados[:] ) # "pessoas[0]" == lista dados1
pessoas.append(dados2[:]) # "pessoas[1]" == lista dados2'''


pessoas = []
dados = []
for _ in range(0,6):
    dados.append(input("Digite um nome: "))
    dados.append(int(input("Digite a idade: ")))
    pessoas.append(dados[:])
    dados.clear()

print(pessoas)

print('As sublistas de pessaos')
for _ in pessoas:
    print(_)
    
print('Todos os nomes das sublistas de pessaos')
for _ in pessoas:
    print(_[0])
    
print('Todas as idades das sublistas de pessaos')    
for _ in pessoas:
    print(_[1])
    
for _ in pessoas:
    
    nomes = _[0]
    idades = _[1]
    print(nomes, idades)
    
    
    
