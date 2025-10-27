
def converter_moeda( moeda_origem, moeda_destino):
    import requests

    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    requisicao = requests.get(link)

    return float(requisicao.json()[f'{moeda_origem}{moeda_destino}']['bid'])

print('Iforme 1 Reais para Dóla\n2 Dóla para Reais')


while True:
    moeda = input('Qual você quer: ')

    if moeda == '1' or moeda == '2':
        
        break
    else:
        print('ERRO: Digite 1 Reais para Dóla\n2 Dóla para Reais')

valor_moeda = float(input("Qual o valor: "))


if moeda == '1':

    moeda_origem = 'USD'
    moeda_destino = 'BRL'

    Moeda = float(converter_moeda(moeda_origem, moeda_destino))

    valor_convertido =valor_moeda / Moeda

elif moeda == '2':
    moeda_origem = 'BRL'
    moeda_destino = 'USD'

    Moeda = float(converter_moeda(moeda_origem, moeda_destino))

    valor_convertido = valor_moeda / Moeda

print(Moeda)

print(f'O valor de {valor_moeda} é {valor_convertido:.2f}')
