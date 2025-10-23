def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2
    return imposto

preco_produto1 = float(input("Qual o preço do primeiro produto: "))
preco_produto2 = float(input("Qual o preço do segumdo produto: "))

imposto_produto1 = calcular_imposto(preco_produto1)
imposto_produto2 = calcular_imposto(preco_produto2)

print(f"O imposto do primeiro produto é {imposto_produto1} e o total é de {imposto_produto1 + preco_produto1}")
print(f"O imposto do segundo produto é {imposto_produto2} e o total é de {imposto_produto2 + preco_produto2}")
