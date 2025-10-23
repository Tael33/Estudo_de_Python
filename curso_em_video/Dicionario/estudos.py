'''pessoas = dict(nome='Tael',idade=20, sexo='M')
print(pessoas)'''

'''print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos e seu sexo é {pessoas["sexo"]}')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''


'''print('======Chaves======')
for chaves in pessoas.keys():
    print(chaves)
print('======valor======')
for valor in pessoas.values():
    print(valor)
print('======Items======')
for item in pessoas.items():
    print(item)

print('======Chaves E Valor======')
for chaves, valor in pessoas.items():
    print(f"{chaves} = {valor}")'''

'''brasil = list()
estado1 = dict(Uf='Rio de Janeiro', sigla='RJ')
estado2 = dict(Uf='Tocantins', sigla='TO')

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['Uf'])
print(brasil[0]['sigla'])
print(brasil[1]['Uf'])
print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()

for _ in range(3):
    estado['UF'] = input('Qual a Unidade Federativa: ')
    estado['Sigla'] = input('Qual a sigla do Estado: ')
    brasil.append(estado.copy())
print(brasil)

for estados in brasil:
    for chave, valor in estados.items():
        print(f"{chave} = {valor}")
    print()






