'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quntidade de dias pelos quais ele foi alugado. Calcule o progreço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

def calcular_preco_aluguel(dias, km):
    """
    Calcula o preço total a pagar pelo aluguel do carro.
    Custo fixo: R$ 60 por dia.
    Custo variável: R$ 0.15 por Km rodado.
    """
    
    custo_dias = dias * 60.0
    
    custo_km = km * 0.15
    
    total_a_pagar = custo_dias + custo_km
    
    return total_a_pagar

print("--- Calculadora de Aluguel de Carro ---")

try:
   
    dias_alugados = int(input("Quantidade de dias alugados: "))
    
   
    km_rodados = float(input("Quantidade de Km percorridos: "))

   
    valor_total = calcular_preco_aluguel(dias_alugados, km_rodados)

    print("\n--- Total a Pagar ---")
    print(f"Custo por {dias_alugados} dias: R$ {dias_alugados * 60.0:.2f}")
    print(f"Custo por {km_rodados} Km: R$ {km_rodados * 0.15:.2f}")
    print(f"O preço total a pagar é: R$ {valor_total:.2f}")

except ValueError:
    print("\nErro! Por favor, digite apenas números válidos para os dias e quilômetros.")