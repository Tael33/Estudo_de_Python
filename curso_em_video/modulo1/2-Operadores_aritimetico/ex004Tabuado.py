num = int(input('Digite um número para ver a sua tabuada: '))
titulo = f"Tabuada {num}"
print(f"{titulo:=^40}", )
for i in range(0, 11):
    print(f'| {num} X {i} = {num * i} |')
