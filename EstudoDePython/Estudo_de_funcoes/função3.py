'''Criação de uma função simples de saudação. A função deverá ter o nome
saudar_usuario, não recebe parâmetros e simplesmente imprimir
"Olá! Bem-vindo ao meu programa.".'''

def saudar_usuario():
    return "Olá! Bem-vindo ao meu programa."


print(saudar_usuario())

#-----------------------------------------------------------------------------------------------------------------------------------------------

''' Criação de uma função personalizada de saudação. A função deverá ter
o nome saudação_ao_usuario, receber como parâmetro o nome e o sexo do
usuário (F ou M) e imprimir: "Olá, <nome>! Bem-vindo ao meu programa.”,
ou "Olá, <nome>! Bem-vinda ao meu programa.” '''

def saudacao_ao_usuario(Nome, Sexo):
    if Sexo.upper() == 'M':
        return f"Olá, {Nome}! Bem-vindo ao meu programa."
    elif Sexo.upper() == 'F':
        return f"Olá, {Nome}! Bem-vinda ao meu programa."

nome = input("Qual o seu nome: ")
sexo = input("Qual o seu sexo 'M' ou 'F': ")

print(saudacao_ao_usuario(nome, sexo))

# -----------------------------------------------------------------------------------------------------------------------------------------------

'''Criação de uma função para conversão de unidades (metros para
centímetros). A função deve receber um valor em metros e retornar o
valor convertido para centímetros.'''

def converter_unidade(metro):
    return metro * 100

metro = float(input('Qual o valor em metros que você quer sabem em centímetro: '))

print (f"O valor {metro}m é equivalente a {converter_unidade(metro):.2f}cm")

'''Criação de uma função para cálculo de média. A função deverá se chamar
calcular_media; essa função deve receber três notas como parâmetros e retornar a
média aritmética delas.'''

def calcular_media(Valor1, Valor2, Valor3, Valor4):
    return (Valor1 + Valor2 + Valor3 + Valor4) / 4

nota1 = float(input("Qual a 1° nota: "))
nota2 = float(input("Qual a 2° nota: "))
nota3 = float(input("Qual a 3° nota: "))
nota4 = float(input("Qual a 4° nota: "))

print(f"A média dos valores {nota1}, {nota2}, {nota3}, {nota4} é {calcular_media(nota1, nota2, nota3, nota4)}")

#------------------------------------------------------------------------------------------------------------------------------------------------

'''Desenvolva uma função para cálculo da área e do perímetro de um círculo. A função
deverá ser chamada dados_circulo, deve receber como parâmetros o raio e a letra “A”
se a informação solicitada for a área do círculo ou “P” se a informação solicitada for o
perímetro do círculo. Considere para o valor de pi, 3.1415.'''

def dados_circulo(Raio, info):
    pi = 3.14159
    if info.upper() == 'A':
        return pi * (Raio**2)
    if info.upper() == 'P':
        return 2 * Raio * pi
    else:
        return f"A informação '{info}' é inválida! digite 'P' para caucular o Perímetro ou 'A' para a Área"

print (f"Círculo de raio 3 tem área: {dados_circulo(3,'A'):.2f}")
print (f"Círculo de raio 5 tem perímetro: {dados_circulo(5,'P'):.2f}")


'''Desenvolva uma função Contador de Vogais. Crie uma função contar_vogais que
recebe uma string e retorna o número de vogais (a, e, i, o, u) presentes nela.'''

def contar_vogais(string):
    vogais = { 'a', 'e', 'i', 'o', 'u',
               'A', 'E', 'I', 'O', 'U',
               'á', 'é', 'í', 'ó', 'ú',
               'Á', 'É', 'Í', 'Ó', 'Ú',
               'â', 'ê', 'ô',
               'Â', 'Ê', 'Ô',
               'ã', 'õ',
               'Ã', 'Õ',
               'à', 'À',
               'ü', 'Ü'
               }

    cont = 0
    for letras in string:
        if letras in vogais:
            cont +=1
    return cont

exp1 = "Python é incrível"

exp2 = "Programar em Python é divertido"

print(f"Temos {contar_vogais(exp1)} vogais na expressão: {exp1}")
print(f"Temos {contar_vogais(exp2)} vogais na expressão: {exp2}")


#------------------------------------------------------------------------------------------------------------------------------------------------


'''Desenvolva uma função para geração de mensagem para um relatório: Crie uma
função gerar_relatorio que recebe os seguintes parâmetros: nome_do_produto,
quantidade e preco_unitario. A função deve calcular o valor total e retornar uma
mensagem formatada do tipo: “Faturamento do produto <nome_do_produto>:
<valor_total_da_venda>.'''

def gerar_relatorio(nome_do_produto, quantidade, preco_unitario):
    valor_total_da_venda = quantidade * preco_unitario
    return f"Faturamento do produto {nome_do_produto}: {valor_total_da_venda}."

vendas = [["iphone",8,5500], ["ipad",3,2000],["note",5,6500]]

for prod, quant, unit in vendas:
    print(gerar_relatorio(prod, quant, unit))

#-----------------------------------------------------------------------------------------------------------------------------------------------


'''Crie uma função de processamento de uma lista. A função deve receber uma lista
cujos elementos são números inteiros positivos ou strings, como no exemplo: [3, 'oi', 5,
7, 'olá' ,10]. A função deverá ignorar todas as strings da lista e retornar a soma dos
números constantes dessa lista.'''

def processar_lista_somar(lista_mista):
    soma = 0
    for element in lista_mista:
        if type(element) == int:
            soma += element
    return soma     

nm_num = [3,'0i',5,7,'0lá',10]
print(f"A soma dos números em {nm_num} é {processar_lista_somar(nm_num)}")


#-----------------------------------------------------------------------------------------------------------------------------------------------
        
'''Elabore um código que valide um login simples com validação. Leia usuário e senha; considere
válido se usuário não for vazio após .strip() e a senha tiver ao menos 6 caracteres e não contiver
espaços entre eles. Exiba “Acesso permitido” ou a razão da recusa. Use apenas avaliações
booleanas e métodos de string.'''

def validar(usuario, senha):
    retorno = []
    if usuario:
        resultado = []
        usuario_format = usuario.strip().split()
        novo_usuario = ''.join(usuario_format)
        valor = True
        resultado.append(novo_usuario)
        resultado.append(valor)
        retorno.append(resultado)
    if senha:
        resultado = []
        senha_format = senha.strip().split()
        nova_senha = ''.join(senha_format)
        
        if len(nova_senha) >= 6:
            valor = True
        else:
            valor = False
        resultado.append(nova_senha)
        resultado.append(valor)
        retorno.append(resultado)
    return retorno

while True:
    usuario = input("Digite o seu nome de usuário: ")
    senha = input("Digite sua senha com no mínimo 6 caracteres: ")

    retorno_validacao = validar(usuario, senha)

    valicacao = True

    if len(retorno_validacao) < 2:
        print("\nERRO: Usuário e senha não podem ser vazios. Tente novamente.\n")
        validacao = False
    for item in retorno_validacao:
        
        nome_campo = item[0]
        statos_campo = item[1]
        
        if nome_campo and statos_campo:
            print(f"Campo: {nome_campo}, 'Válido';")
        else:
            print(f"Campo: {nome_campo} 'Inválido'; Tente novamente.\n")
            validacao = False

    if valicacao:
        print("\n✅ Usuário e senha validados com sucesso!\n")
        break
    else:
        print("\n❌ Dados inválidos. Por favor, digite novamente.\n")


        
#------------------------------------------------------------------------------------------------------------------------------------------------                 

'''Elabore um código que leia uma lista de nomes (separados por vírgula), gere e imprima outra
lista contendo apenas os nomes que começam com vogal (A, E, I, O, U), ignorando
maiúsculas/minúsculas.'''


def começa_vogal_consoantes(lista):

    vogais = { 'a', 'e', 'i', 'o', 'u',
               'A', 'E', 'I', 'O', 'U',
               'á', 'é', 'í', 'ó', 'ú',
               'Á', 'É', 'Í', 'Ó', 'Ú',
               'â', 'ê', 'ô',
               'Â', 'Ê', 'Ô',
               'ã', 'õ',
               'Ã', 'Õ',
               'à', 'À',
               'ü', 'Ü'
               }
    nomes_vogal = []
    nomes_consoantes = []
    resultados = []
    
    for nome in lista:

        if nome[0] in vogais:
            nomes_vogal.append(nome)
        else:
            nomes_consoantes.append(nome)
    resultados.append(nomes_vogal)
    resultados.append(nomes_consoantes)
    
    return resultados

nomes = ["Ana","Bruno","Camila","Daniel","Eduardo","Fernanda","Gabriel","Helena","Isabela","João",
    "Laura","Marcos","Olívia","Patrícia","Arthur","Renata","Sérgio","Igor","Vanessa","Amanda"
]

print(começa_vogal_consoantes(nomes))


dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

#------------------------------------------------------------------------------------------------------------------------------------------------

'''Exercício 1: Consolidação de Estoque de Duas Lojas
Contexto: Você trabalha em uma empresa que tem dois depósitos, e os estoques de cada um
estão em listas separadas. Sua tarefa é criar uma função que consolide o estoque em uma única lista,
somando as quantidades de itens que aparecem em ambos os depósitos.

Tarefa:

Crie uma função chamada consolidar_estoques.

A função deve receber duas listas como parâmetros: estoque_loja_A e estoque_loja_B.

A função deve retornar uma única lista de estoque consolidado.

Se um item existe apenas em uma das listas, ele deve ser copiado para a lista final.

Se um item existe em ambas as listas, suas quantidades devem ser somadas na lista final.'''


def consolidar_estoques(estoque_loja_A, estoque_loja_B):
    estoque_final = []
    for item_a in estoque_loja_A:
            estoque_final.append(item_a)
            
    for item_b in estoque_loja_B:
        produto = item_b[0]
        quant = item_b[1]
        
        for item_final in estoque_final:
            if item_final[0] == produto:
                item_final[1] += quant
                break
        if not item_b in estoque_final:
            estoque_final.append(item_b)
    return sorted(estoque_final)
                


estoque_loja_A = [
    ["Mochila", 12],
    ["Barraca", 8],
    ["Lanterna", 35]
]

estoque_loja_B = [
    ["Lanterna", 20],
    ["Bota", 15],
    ["Mochila", 10]
]

print(consolidar_estoques(estoque_loja_A, estoque_loja_B))


#2 --------------------------------------------------------------------------------------------------------------------------------------------------

'''Exercício 2: Gerar Relatório de Notas de Alunos
Contexto: Você tem uma lista com os nomes dos alunos e as suas notas em três provas.
Você precisa calcular a média de cada aluno e
determinar se ele foi aprovado ou reprovado.

Tarefa:

Escreva uma função chamada gerar_relatorio_final.

A função deve receber uma lista de alunos, onde cada sublista contém
o nome do aluno seguido por suas três notas.

A função deve retornar uma nova lista, onde cada sublista contém
o nome do aluno e sua situação final ("Aprovado" ou "Reprovado").

Considere que a média para aprovação é 7.0.'''

def gerar_relatorio_final(alunos):
    resultado_final = []
    for _ in alunos:
        
        pessoa = _[0]
        nota1 = _[1]
        nota2 = _[2]
        nota3 = _[3]

        media = (nota1 + nota2 + nota3) / 3

        if media >= 7:
            status = "Aprovado"
        else:
            status = "Reprovado"
        
        resultado_final.append([pessoa, round(media, 1), status])

    return sorted(resultado_final)

alunos_nota = [
    ["Ana", 8.0, 7.5, 9.0],
    ["Bruno", 5.0, 6.5, 7.0],
    ["Carla", 9.5, 8.5, 10.0],
    ["Daniel", 4.0, 5.0, 6.0]
]

print(gerar_relatorio_final(alunos_nota))

#3 --------------------------------------------------------------------------------------------------------------------------------------------------

def contar_estoque_baixo(inventario, quantidade_minima):
    contador = 0
    for i in range(len(inventario)):
        if inventario[i][1] < quantidade_minima:
            contador += 1
    return contador
def contar_estoque_baixo2(inventario, quantidade_minima):
    produtos_estoque = []

    for item in inventario:

        produto = item[0]
        quantidade_produto = item[1]

        if quantidade_produto <= quantidade_minima:
            status = "Baixo"
        else:
            status = "Suficiente"
        produtos_estoque.append([produto, quantidade_produto, status])
    return sorted(produtos_estoque)
            

inventario = [
    ["Mochila", 12],
    ["Barraca", 8],
    ["Lanterna", 35],
    ["Bota", 5]
]

print(f"Produtos com estoque baixo: {contar_estoque_baixo(inventario, 10)}")
print(f"Produtos com estoque baixo: \n")
for item in contar_estoque_baixo2(inventario, 10):
    produto = item[0]
    quantidade_produto = item[1]
    status = item[2]
    print(F'Produto: {produto}, Quantidade: {quantidade_produto}, Status: {status}')




