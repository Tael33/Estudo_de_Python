# Desafio 1: Análise de Dados com while e if
# Crie um programa que use um laço while para ler a idade e 
# o preço do ingresso pago por um número indeterminado de visitantes de um museu. 
# O laço deve parar quando o usuário digitar 0 para a idade.

# Ao final, o programa deve informar:

# Quantas pessoas pagaram ingresso.

# A média de idade das pessoas que pagaram.

# Quantas pessoas eram "maiores de idade" (idade >= 18).

# Quantas pessoas eram "menores de idade" (idade < 18).


def analisar_dados():
 

    return

def iniciar():
    dados_clientes = list()
    while True:

        precoIngrsso = float(input('Qual o preço que o cliente pagou no ingresso: '))
        idade = int(input('Qual a idade o criente: '))

        if idade == 0:
            break

        cliente = [idade, precoIngrsso]

        dados_clientes.append(cliente)

        print("--- Dicionário atualizado ---")
        print(criar_dict(dados_clientes))

    print("\n--- Dicionário FINAL ---")
    print(criar_dict(dados_clientes))


def criar_dict(lista: list):
    dados_clientes_dict = dict()  

    for i, dados in enumerate(lista):

        idd, precoIngrsso = dados

        cliente = dict(idade = idd, valorIngresso = precoIngrsso)

        dados_clientes_dict [i+1] = cliente

    return dados_clientes_dict


iniciar()
print(analisar_dados())
