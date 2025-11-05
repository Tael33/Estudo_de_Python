# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o proço da passagem, cobrando R$0,50 por Km para viagens de até
# 200Km e R$0,45 para viagens mais longe.

distancia = float(input('Qual a distancia da sua viagem em Km: '))

if distancia <= 200:
    print(f'O valr para {distancia}Km é de R${distancia * 0.5}')
else:
    print(f'O valor para {distancia}Km é de R${distancia * 0.45}')