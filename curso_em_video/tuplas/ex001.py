# o Cria um progama que tenha uma tupla totalmente
# preenchida com uma contagem por extaenso. de zero até
# vinta.

# Sau programa deverá ler um número palo taclado (entre O e 20)
# e mostrá-lo por extenso.

numeros_por_extenso = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte"
)
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 and num <= 20:
        print(f"Você digitou o número {numeros_por_extenso[num]}").lower()
        resposta = input("Digete 's' para continuar ou qualquer tecla para sair:")
        if resposta != 's':
            break 
    print("Tente novamente.")

    
    