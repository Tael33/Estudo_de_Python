#with open ('teste1.txt', 'w', encoding = 'UTF-8') as arq:
    #arq.write('Olá, Mundo\n')
    #arq.write('Essa é a segunda linha\n')

#with open ('teste1.txt', 'r', encoding = 'UTF-8') as arq:
    #result = arq.readable()
    #print(result)

# with open ('corrida.txt', 'w', encoding = 'UTF-8') as arq:

#     while True:

#         NumCorredor = input('Qual o Número do corredor: ')
#         if NumCorredor == '000':
#             break

#         NomeDoCorredor = input('Qual o nome do corredor: ')
#         IddDoCorredor = input('Qual a idade do corredor: ')
#         VelocidDoCorrdor = input('Qual a velocidade do corredor: ')

#         arq.write(f'{NumCorredor}; {NomeDoCorredor}; {IddDoCorredor}; {VelocidDoCorrdor}\n')

# cop_arq = list
# with open('corrida.txt', 'r', encoding = 'utf-8') as arq:

#     cop_arq = arq.read()

# print(cop_arq)


# with open ('corrida2.txt', 'w', encoding = 'utf-8') as arq:
#     arq.write(cop_arq)

with open ('corrida2.txt', 'r', encoding = 'utf-8') as arq:
    
    conteudo = arq.readlines()
    
    print(conteudo)
    
    for linhas in conteudo:
        
        dados = linhas.strip().split(';')

        cod = dados[0]
        nome = dados[1]
        idd = dados[2]
        velo = dados[3]

        print(f'O(a) corredor(a) {nome} do código {cod} tem {idd} anos e sua velocidade foi de {velo}')
       
        



        


def criar_dict(arq):
    corrida_dict = dict()

    with open (arq, 'r', encoding = 'utf-8') as arquivo:


        conteudo = arquivo.readlines()
        for linhas in conteudo:
            dados = linhas.strip().split(';')
            cod, nome, _ , _ = linhas.strip().split(';')
            corrida_dict[cod] = nome
        
    return corrida_dict

#print (criar_dict('corrida2.txt'))
