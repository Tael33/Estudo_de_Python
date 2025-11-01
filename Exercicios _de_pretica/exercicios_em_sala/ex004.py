def adicionar_animais():

    with open('g:/Engenharia_de_Software/Estudo_de_Pytho/Exercicios _de_pretica/exercicios_em_sala/animais.txt', 'a', encoding='utf-8') as arq:

        while True:

            cod = input('Digite o códico do animal: ')
            if cod == '000':
                break
            animal = input('Digite o Nome do animmal: ').title()

            arq.write(f'{cod}-{animal}\n')
            
adicionar_animais()