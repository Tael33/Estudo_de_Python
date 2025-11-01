def criar_arquivo(lista: list):

    with open('G:/Engenharia_de_Software/Estudo_de_Pytho/Exercicios _de_pretica/exercicios_em_sala/codigos.txt', 'w', encoding='utf-8') as arq:
        
        for dados in lista:
            cod, num = dados
            arq.write(f'{cod}; {num[0]}; {num[1]}; {num[2]}\n' )



lista = [('CD-12', (2,3,4)), 
         ('WD-23', (9,8,7)), 
         ('RT-56', (7,6,4)) ]
criar_arquivo(lista)