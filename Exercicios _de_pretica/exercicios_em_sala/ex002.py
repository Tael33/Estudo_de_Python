def cod_zoo(arquivo):
    dict_zoo = dict()

    with open(arquivo, 'r', encoding='utf-8') as arq:

        for linha in arq:

            dados = linha.strip().split('-')

            chave, animal = dados

            dict_zoo[chave] = animal
            

print(cod_zoo('g:/Engenharia_de_Software/Estudo_de_Pytho/Exercicios _de_pretica/exercicios_em_sala/animais.txt'))