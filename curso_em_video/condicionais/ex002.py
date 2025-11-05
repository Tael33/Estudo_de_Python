# crie um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$7,00 por cada Km acima do limite.


velo = float(input('Qual a velocidade do carro: '))

if velo > 80:
    print(f'Sua velocidade é de {velo}, Você foi multado!\nSua multa é de {(velo-80) * 7.00}')
else:
    print('Você está dentro da velocidade permitida!')