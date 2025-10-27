'''Faça um programa que leia a altura de uma parede em metros , calcule a sua área e a quantidade de tinta necessária para pinta-la,
sabendo que a cada litro de tinta, pinta uma área de 2m².'''

def caucular_area(largura, altura):
    area = largura * altura
    LitroTinta = 2
    return area, area/LitroTinta



altura = float(input('Digite a altura da para em metros: '))
largura = float(input('Digite a largura da parede: '))

area, quanTinta = caucular_area(altura, largura)

print(f'A área de sua parede é {area} e quantidade de tinta para uma demão de tinta é {quanTinta}')


