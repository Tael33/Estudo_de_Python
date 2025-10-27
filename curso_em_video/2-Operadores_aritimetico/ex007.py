'''Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto'''

precoProduto = float(input('Digite o preço do produto pra receber 5% de desconto: '))

novoPreco = precoProduto - (precoProduto * 0.05)

print(f'Seu novo preço com desconto é {novoPreco}')
                     