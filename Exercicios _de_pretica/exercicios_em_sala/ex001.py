def criar_lista(arquivo):
    lista = list()
    with open(arquivo, 'r', encoding='utf-8') as arq:
        print(arq)
        for linha in arq:

            item = linha.strip().title()

            if item.isnumeric():
                lista.append(int(item))

            else:

                lista.append(linha.strip().title())

    lista.sort()      

    return lista


print(criar_lista('g:/Engenharia_de_Software/Estudo_de_Pytho/Exercicios _de_pretica/exercicios_em_sala/nomes.txt'))

print(criar_lista('g:/Engenharia_de_Software/Estudo_de_Pytho/Exercicios _de_pretica/exercicios_em_sala/numeros.txt'))


