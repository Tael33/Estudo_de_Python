# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, 
# de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

notas = list()

for _ in range(4):
    nota = float(input(f'Qual a sea {_+1}° nota: '))
    notas.append(nota)

for nota in notas:
    soma += nota

print(f'Sua média é {soma / len(notas):.}')