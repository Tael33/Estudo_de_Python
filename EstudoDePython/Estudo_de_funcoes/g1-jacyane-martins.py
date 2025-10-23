
def maratonistas_potencial(lista1, km):
        maiores = 0
        for i in range(len(lista1)):
            if lista1[i][2] > km:
                maiores += 1
        return maiores


def tempo_total(lista2):
    total_min = 0
    for i in range(len(lista2)):
        total_min += lista2[i][1]
    return total_min


def calculo_desempenho(lista3):
    for i in range(len(lista3)):
        listapace = []
        pace = print(f"'Usuário{i+1}', {lista3[i][1] / lista3[i][2]:.2f}")
        listapace.append(pace)
    return listapace
        
     
    
# a - 
lista1 = [['Usuario 1', 22, 11.1],['Usuario 2', 12, 6.7],['Usuario 3', 12, 15.7]]
print(maratonistas_potencial(lista1, 10))
print("_"*10)

# b -
lista2 = [['Usuario 1', 22, 11.1],['Usuario 2', 12, 6.7],['Usuario 3', 12, 15.7]]
print(f"Tempo total em minutos: {tempo_total(lista2)}")
print("_"*10)

# c -
lista3 = [['Usuario 1', 22, 11.1],['Usuario 2', 12, 6.7],['Usuario 3', 12, 15.7]]
calculo_desempenho(lista3)

print("_"*20)

# 2 ----------------------------------------------------------------------------------

def validar_acesso(usuario, autorizados):
    for i in range(len(autorizados)):
        if "AB123" in autorizados or "CD456" in autorizados or "EG789" in autorizados:
            return True
        else:
            return False

def imprimir_inventario(inventario):
    for i in range(len(inventario)):
        print(f"{inventario[i][0]} | {inventario[i][1]}")

def verificar_reposicao(inventario, qt):
    for i in range(len(inventario)):
        if qt < inventario[i][1]:
            print(f"ALERTA DE REPOSIÇÃO: O Produto {inventario[i][0]} está com apenas {inventario[i][1]} unidades.")

def lista_materiais(inventario):
    for i in range(len(inventario)):
        return inventario.remove([i][0]) .sort()

    
# a -  
autorizados = ["AB123", "CD456", "EG789"]
inventario = [["Mochila", 12],["Barraca", 8],["Lanterna", 35],["Bota", 5],["Cantil", 22]]

usuario = input("Digite seu acesso: ").strip() .upper()
print(validar_acesso(usuario, autorizados))

# b -
inventario = [["Mochila", 12],["Barraca", 8],["Lanterna", 35],["Bota", 5],["Cantil", 22]]
imprimir_inventario(inventario)

# c -
qt = int(input("Defina o estoque mínimo: "))
verificar_reposicao(inventario, qt)

# d -

inventario = [["Mochila", 12],["Barraca", 8],["Lanterna", 35],["Bota", 5],["Cantil", 22]]
print(lista_materiais(inventario))





















































