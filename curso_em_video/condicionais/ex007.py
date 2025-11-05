# o Escreva um programa que pergunta o salário de um 
# Funcionário e calcule o valor do seu aumento.

# Para salários
# superiores a
# R$1.250.00. calcule um
# aumento de 10%.

# Para os inferiores ou iguais, 
# o aumento é de 15%

def calcular_salario(salario):

    salario_medio = 1250.00
    if salario <= salario_medio:
        return (salario * 0.15) + salario
    else:
        return (salario * 0.10) + salario

salario = float(input('Qual o salário: '))

print(f'O salário R${salario} com aumento é de {calcular_salario(salario)}')