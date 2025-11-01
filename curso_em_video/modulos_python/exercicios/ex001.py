import random

def sortear_aluno(lista: list):
    
    nome_sorteado = random.choice(lista)
    
    return nome_sorteado
def sortear_alunos(lista: list):
    random.shuffle(lista)
    return lista

nomes = ['Pedro', 'Vitoria', 'Arthur', 'Tael']

# for _ in range(4):
#     nome = input(f'Digite o {_+1}° nome: ')

#     nomes.append(nome)

print(f'O aluno sorteado é {sortear_aluno(nomes)}')

print(f'A sequencia de alunos é {sortear_alunos(nomes)}')

