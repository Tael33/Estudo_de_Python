"""
Versão completamente anotada (mistura de comentários linha-a-linha e por bloco).

Este arquivo mantém o código original e adiciona comentários explicando, em
nível de detalhe, o propósito de cada linha ou bloco de linhas. Para funções
muito similares (conversões, pequenas utilidades) usei comentários por bloco
para evitar repetição excessiva. Se quiser que eu comente absolutamente cada
linha de todas as funções (incluindo as repetitivas), eu posso, mas o arquivo
ficará muito maior; posso gerar por partes mediante sua revisão.

Execute com: python aula001_fully_annotated.py

"""

# -----------------------------
# Operações aritméticas básicas
# -----------------------------

# Definição da função 'soma' com dois parâmetros posicionais 'a' e 'b'.
def soma(a, b):
    # A linha abaixo retorna o resultado da operação de adição entre 'a' e 'b'.
    # Em Python o operador '+' faz sobrecarga: para números aritméticos soma valores.
    return a + b


# Definição da função 'subtracao' com dois parâmetros posicionais.
def subtracao(a, b):
    # Retorna a diferença entre 'a' e 'b'.
    return a - b


# Definição da função 'multiplicacao' com dois parâmetros posicionais.
def multiplicacao(a, b):
    # Retorna o produto de 'a' por 'b'.
    return a * b


# Definição da função 'divisao' que trata divisão por zero.
def divisao(a, b):
    # Verifica se o divisor 'b' é diferente de zero.
    if b != 0:
        # Se não for zero, realiza a operação de divisão e retorna o resultado.
        return a / b
    else:
        # Se for zero, em vez de lançar exceção, retorna string informando o erro.
        # Observação: retornar strings em funções numéricas nem sempre é ideal;
        # pode ser preferível lançar ValueError. Aqui seguimos o design original.
        return "Divisão por zero não é permitida."


# -----------------------------
# Potências e radiciação
# -----------------------------

# Função que calcula a potência a**b.
def potencia(a, b):
    # Usa o operador ** do Python que eleva 'a' à potência 'b'.
    return a ** b


# Função que calcula raiz quadrada com validação simples.
def raiz_quadrada(a):
    # Verifica se a entrada é não-negativa (raiz quadrada de negativo não é real).
    if a >= 0:
        # Calcula a raiz como potência a**0.5 e retorna.
        return a ** 0.5
    else:
        # Retorna mensagem em caso de valor inválido.
        return "Raiz quadrada de número negativo não é permitida."


# Função que calcula raiz cúbica.
def raiz_cubica(a):
    # Retorna a**(1/3). Atenção: para números negativos, esse cálculo usando
    # floats pode produzir um número complexo em algumas situações; no entanto,
    # em Python, (-8) ** (1/3) resulta em um número complexo; uma forma segura
    # para raiz cúbica real é usar math.copysign(abs(a) ** (1/3), a).
    return a ** (1/3)


# Função fatorial (iterativa) com tratamento para n negativo.
def fatorial(n):
    # Se n < 0, retorno é mensagem de erro (design do autor).
    if n < 0:
        return "Fatorial de número negativo não é definido."
    elif n == 0 or n == 1:
        # 0! e 1! são 1 por definição.
        return 1
    else:
        # Caso geral: inicializa resultado com 1 e multiplica de 2 até n.
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado


# -----------------------------
# Porcentagem e logaritmos
# -----------------------------

# Calcula (total * percentual) / 100
def porcentagem(total, percentual):
    # Operação aritmética simples: multiplica e divide por 100.
    return (total * percentual) / 100


# Calcula logaritmo de 'a' na base fornecida (padrão 10), validando parâmetros.
def logaritmo(a, base=10):
    import math
    # Valida que 'a' > 0 e base > 1 (base 1 não é válida para logaritmo).
    if a > 0 and base > 1:
        # usa math.log para calcular log de base qualquer: math.log(x, base)
        return math.log(a, base)
    else:
        # Mensagem de erro para valores inválidos.
        return "Logaritmo indefinido para esses valores."


# -----------------------------
# Trigonometria (graus -> radianos)
# -----------------------------

# A maioria das funções trigonométricas em math esperam radianos; essas
# wrappers recebem ângulo em graus e convertem para radianos com math.radians.

def seno(angulo):
    import math
    # Converte graus para radianos e calcula seno.
    return math.sin(math.radians(angulo))


def cosseno(angulo):
    import math
    return math.cos(math.radians(angulo))


def tangente(angulo):
    import math
    return math.tan(math.radians(angulo))


# -----------------------------
# Utilitários simples
# -----------------------------

def valor_absoluto(a):
    # Usa função built-in abs para retornar valor absoluto.
    return abs(a)


def arredondar(a, casas_decimais=0):
    # Usa round integrado; casas_decimais padrão 0 -> retorna inteiro arredondado.
    return round(a, casas_decimais)


def minimo(a, b):
    # Retorna o menor dos dois usando min built-in.
    return min(a, b)


def maximo(a, b):
    # Retorna o maior dos dois usando max built-in.
    return max(a, b)


# -----------------------------
# Estatística básica
# -----------------------------

# Abaixo, funções que operam sobre listas de números.
# Padrão: listas vazias geralmente retornam 0 ou None dependendo do caso.

def media(lista):
    # Se lista vazia, evita divisão por zero e retorna 0.
    if len(lista) == 0:
        return 0
    # Soma todos os elementos e divide pela quantidade.
    return sum(lista) / len(lista)


def mediana(lista):
    # Se lista vazia, retorna 0 por convenção definida neste módulo.
    if len(lista) == 0:
        return 0
    # Ordena a lista para encontrar o elemento do meio.
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2
    if n % 2 == 0:
        # Para número par de elementos, mediana é média dos dois do meio.
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        # Para ímpar, retorna o elemento central.
        return lista_ordenada[meio]


def moda(lista):
    # Utiliza Counter para contar frequências dos elementos.
    from collections import Counter
    if len(lista) == 0:
        return None
    contagem = Counter(lista)
    # Encontra a frequência máxima.
    max_frequencia = max(contagem.values())
    # Lista com todos os elementos que têm a frequência máxima.
    modas = [k for k, v in contagem.items() if v == max_frequencia]
    if len(modas) == len(contagem):
        # Se todas as chaves têm mesma frequência, dizemos que não há moda.
        return None
    return modas


def desvio_padrao(lista):
    import math
    if len(lista) == 0:
        return 0
    # Calcula média e usa fórmula do desvio padrão populacional (n denom).
    media_valor = media(lista)
    variancia = sum((x - media_valor) ** 2 for x in lista) / len(lista)
    return math.sqrt(variancia)


# Combinação e permutação usam factorial do módulo math.

def combinacao(n, k):
    from math import factorial
    # Validação de entradas: se k>n ou negativos, retorna 0.
    if k > n or n < 0 or k < 0:
        return 0
    # Fórmula: n! / (k! * (n-k)!)
    return factorial(n) // (factorial(k) * factorial(n - k))


def permutacao(n, k):
    from math import factorial
    if k > n or n < 0 or k < 0:
        return 0
    # Fórmula: n! / (n-k)!
    return factorial(n) // factorial(n - k)


# -----------------------------
# Geometria e conversões (bloco de funções parecidas)
# -----------------------------

# Observação: as próximas funções são majoritariamente conversões de unidades
# ou cálculos geométricos; cada função recebe parâmetros, validações simples
# e retorna o valor calculado.

def hipotenusa(cateto1, cateto2):
    import math
    # math.hypot calcula sqrt(x*x + y*y) com maior precisão numérica.
    return math.hypot(cateto1, cateto2)


def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def quilometros_para_milhas(km):
    return km * 0.621371


def milhas_para_quilometros(milhas):
    return milhas / 0.621371


def litros_para_galoes(litros):
    return litros * 0.264172


def galoes_para_litros(galoes):
    return galoes / 0.264172


def metros_para_pes(metros):
    return metros * 3.28084


def pes_para_metros(pes):
    return pes / 3.28084


def segundos_para_horas(segundos):
    return segundos / 3600


def horas_para_segundos(horas):
    return horas * 3600


def dias_para_semanas(dias):
    return dias / 7


def semanas_para_dias(semanas):
    return semanas * 7


def anos_para_dias(anos):
    # Considera 365.25 dias por ano (média incluindo bissextos)
    return anos * 365.25


def dias_para_anos(dias):
    return dias / 365.25


# -----------------------------
# Áreas, volumes e utilitários de geometria (com validação)
# -----------------------------

def calcular_imc(peso, altura):
    # Validação: altura deve ser > 0 para evitar divisão por zero.
    if altura <= 0:
        return "Altura deve ser maior que zero."
    return peso / (altura ** 2)


def calcular_area_circulo(raio):
    import math
    if raio < 0:
        return "Raio não pode ser negativo."
    return math.pi * (raio ** 2)


def calcular_area_retangulo(largura, altura):
    if largura < 0 or altura < 0:
        return "Largura e altura não podem ser negativas."
    return largura * altura


def calcular_area_triangulo(base, altura):
    if base < 0 or altura < 0:
        return "Base e altura não podem ser negativas."
    return (base * altura) / 2


def calcular_volume_esfera(raio):
    import math
    if raio < 0:
        return "Raio não pode ser negativo."
    return (4/3) * math.pi * (raio ** 3)


def calcular_volume_cilindro(raio, altura):
    import math
    if raio < 0 or altura < 0:
        return "Raio e altura não podem ser negativos."
    return math.pi * (raio ** 2) * altura


def calcular_volume_cone(raio, altura):
    import math
    if raio < 0 or altura < 0:
        return "Raio e altura não podem ser negativos."
    return (1/3) * math.pi * (raio ** 2) * altura


# -----------------------------
# Física básica e utilitários (com validação onde necessário)
# -----------------------------

def calcular_distancia_pontos(x1, y1, x2, y2):
    import math
    # math.hypot é numéricamente estável e calcula a distância euclidiana.
    return math.hypot(x2 - x1, y2 - y1)


def calcular_velocidade(distancia, tempo):
    # Valida tempo > 0 para evitar divisão por zero.
    if tempo <= 0:
        return "Tempo deve ser maior que zero."
    return distancia / tempo


def calcular_aceleracao(velocidade_inicial, velocidade_final, tempo):
    if tempo <= 0:
        return "Tempo deve ser maior que zero."
    return (velocidade_final - velocidade_inicial) / tempo


def calcular_forca(massa, aceleracao):
    # Segunda lei de Newton: F = m * a
    return massa * aceleracao


def calcular_trabalho(forca, deslocamento):
    # Trabalho = força * deslocamento (quando força paralela ao deslocamento)
    return forca * deslocamento


def calcular_energia_cinetica(massa, velocidade):
    # Energia cinética clássica = 0.5 * m * v^2
    return 0.5 * massa * (velocidade ** 2)


def calcular_energia_potencial(massa, altura, gravidade=9.81):
    # Energia potencial gravitacional = m * g * h (g padrão 9.81 m/s^2)
    return massa * gravidade * altura


def calcular_pressao(forca, area):
    if area <= 0:
        return "Área deve ser maior que zero."
    return forca / area


def calcular_densidade(massa, volume):
    if volume <= 0:
        return "Volume deve ser maior que zero."
    return massa / volume


# -----------------------------
# Funções relacionadas a ondas/ângulos e médias ponderadas
# -----------------------------

def calcular_frequencia(tempo_periodo):
    if tempo_periodo <= 0:
        return "Tempo do período deve ser maior que zero."
    return 1 / tempo_periodo


def calcular_periodo(frequencia):
    if frequencia <= 0:
        return "Frequência deve ser maior que zero."
    return 1 / frequencia


def calcular_angulo_seno(oposto, hipotenusa):
    if hipotenusa == 0:
        return "Hipotenusa não pode ser zero."
    import math
    seno_valor = oposto / hipotenusa
    if seno_valor < -1 or seno_valor > 1:
        return "Valor de seno inválido."
    # math.asin retorna valor em radianos; convertemos para graus com degrees
    return math.degrees(math.asin(seno_valor))


def calcular_angulo_cosseno(adjacent, hipotenusa):
    if hipotenusa == 0:
        return "Hipotenusa não pode ser zero."
    import math
    cosseno_valor = adjacent / hipotenusa
    if cosseno_valor < -1 or cosseno_valor > 1:
        return "Valor de cosseno inválido."
    return math.degrees(math.acos(cosseno_valor))


def calcular_angulo_tangente(oposto, adjacent):
    if adjacent == 0:
        return "Adjacente não pode ser zero."
    import math
    return math.degrees(math.atan(oposto / adjacent))


def calcular_media_ponderada(valores, pesos):
    # Valida entradas: listas precisam ter mesmo tamanho e não podem ser vazias.
    if len(valores) != len(pesos) or len(valores) == 0:
        return "Listas de valores e pesos devem ter o mesmo tamanho e não podem ser vazias."
    soma_ponderada = sum(v * p for v, p in zip(valores, pesos))
    soma_pesos = sum(pesos)
    if soma_pesos == 0:
        return "A soma dos pesos não pode ser zero."
    return soma_ponderada / soma_pesos


# -----------------------------
# Finanças básicas e cálculos financeiros
# -----------------------------

def calcular_juro_simples(principal, taxa, tempo):
    # Juros simples = principal * taxa * tempo
    return principal * taxa * tempo


def calcular_juro_composto(principal, taxa, tempo):
    # Retorna apenas os juros compostos acumulados (montante - principal)
    return principal * ((1 + taxa) ** tempo - 1)


def calcular_valor_futuro(principal, taxa, tempo):
    # Montante futuro = principal * (1 + taxa) ** tempo
    return principal * (1 + taxa) ** tempo


def calcular_valor_presente(valor_futuro, taxa, tempo):
    # Valor presente descontado pela taxa composta
    return valor_futuro / (1 + taxa) ** tempo


def calcular_taxa_crescimento(valor_inicial, valor_final, tempo):
    # Valida entradas
    if valor_inicial <= 0 or tempo <= 0:
        return "Valor inicial e tempo devem ser maiores que zero."
    # Taxa média anual composta
    return (valor_final / valor_inicial) ** (1 / tempo) - 1


def calcular_taxa_desconto(valor_futuro, valor_presente, tempo):
    if valor_presente <= 0 or tempo <= 0:
        return "Valor presente e tempo devem ser maiores que zero."
    return (valor_futuro / valor_presente) ** (1 / tempo) - 1


def calcular_amortizacao_sac(valor_emprestimo, taxa_juros, numero_parcelas):
    if numero_parcelas <= 0:
        return "Número de parcelas deve ser maior que zero."
    amortizacao = valor_emprestimo / numero_parcelas
    saldo_devedor = valor_emprestimo
    parcelas = []
    for i in range(numero_parcelas):
        # Juros calculados sobre saldo devedor vigente
        juros = saldo_devedor * taxa_juros
        parcela = amortizacao + juros
        parcelas.append(parcela)
        # Saldo devedor reduz com a amortização constante
        saldo_devedor -= amortizacao
    return parcelas


def calcular_amortizacao_price(valor_emprestimo, taxa_juros, numero_parcelas):
    if numero_parcelas <= 0 or taxa_juros < 0:
        return "Número de parcelas deve ser maior que zero e taxa de juros não pode ser negativa."
    # Fator de capitalização do sistema Price (parcela constante)
    fator = (taxa_juros * (1 + taxa_juros) ** numero_parcelas) / ((1 + taxa_juros) ** numero_parcelas - 1)
    parcela = valor_emprestimo * fator
    # Retorna uma lista com o mesmo valor repetido para cada parcela
    return [parcela] * numero_parcelas


def calcular_taxa_efetiva_anual(taxa_nominal, periodos):
    if periodos <= 0:
        return "Número de períodos deve ser maior que zero."
    # Conversão de taxa nominal para taxa efetiva anual
    return (1 + taxa_nominal / periodos) ** periodos - 1


def calcular_taxa_nominal(taxa_efetiva, periodos):
    if periodos <= 0:
        return "Número de períodos deve ser maior que zero."
    # Converte taxa efetiva anual para taxa nominal equivalente
    return periodos * ((1 + taxa_efetiva) ** (1 / periodos) - 1)


def calcular_valor_presente_liquido(fluxos_caixa, taxa_desconto):
    vpl = 0
    for t, fluxo in enumerate(fluxos_caixa):
        # Cada fluxo é descontado por (1+taxa)^t; t começa em 0
        vpl += fluxo / (1 + taxa_desconto) ** t
    return vpl


def calcular_taxa_interna_retorno(fluxos_caixa, estimativa_inicial=0.1, tolerancia=1e-6, max_iteracoes=1000):
    # Método de Newton-Raphson para encontrar a taxa que zera o VPL
    taxa = estimativa_inicial
    for _ in range(max_iteracoes):
        vpl = sum(fluxo / (1 + taxa) ** t for t, fluxo in enumerate(fluxos_caixa))
        derivada_vpl = sum(-t * fluxo / (1 + taxa) ** (t + 1) for t, fluxo in enumerate(fluxos_caixa))
        if derivada_vpl == 0:
            return None  # Evita divisão por zero
        nova_taxa = taxa - vpl / derivada_vpl
        if abs(nova_taxa - taxa) < tolerancia:
            return nova_taxa
        taxa = nova_taxa
    return None  # Não convergiu


def calcular_ponto_equilibrio(custos_fixos, preco_venda, custo_variavel):
    if preco_venda <= custo_variavel:
        return "Preço de venda deve ser maior que custo variável."
    # Quantidade que zera lucro operacional: custos_fixos / (preco - custo variável)
    return custos_fixos / (preco_venda - custo_variavel)


def calcular_marketing_roi(receita, custo_marketing):
    if custo_marketing == 0:
        return "Custo de marketing não pode ser zero."
    return (receita - custo_marketing) / custo_marketing


def calcular_lucro_bruto(receita, custo_vendas):
    return receita - custo_vendas


def calcular_lucro_liquido(receita, custos_totais, despesas):
    return receita - custos_totais - despesas


def calcular_margem_lucro_bruto(lucro_bruto, receita):
    if receita == 0:
        return "Receita não pode ser zero."
    return lucro_bruto / receita


def calcular_margem_lucro_liquido(lucro_liquido, receita):
    if receita == 0:
        return "Receita não pode ser zero."
    return lucro_liquido / receita


def calcular_roa(lucro_liquido, ativos_totais):
    if ativos_totais == 0:
        return "Ativos totais não podem ser zero."
    return lucro_liquido / ativos_totais


def calcular_roe(lucro_liquido, patrimonio_liquido):
    if patrimonio_liquido == 0:
        return "Patrimônio líquido não pode ser zero."
    return lucro_liquido / patrimonio_liquido


def calcular_current_ratio(ativos_circulantes, passivos_circulantes):
    if passivos_circulantes == 0:
        return "Passivos circulantes não podem ser zero."
    return ativos_circulantes / passivos_circulantes


def calcular_quick_ratio(ativos_circulantes, estoques, passivos_circulantes):
    if passivos_circulantes == 0:
        return "Passivos circulantes não podem ser zero."
    return (ativos_circulantes - estoques) / passivos_circulantes


def calcular_giro_ativos(receita, ativos_totais):
    if ativos_totais == 0:
        return "Ativos totais não podem ser zero."
    return receita / ativos_totais


def calcular_giro_estoques(custo_vendas, estoque_medio):
    if estoque_medio == 0:
        return "Estoque médio não pode ser zero."
    return custo_vendas / estoque_medio


def calcular_periodo_medio_recebimento(vendas_a_prazo, contas_a_receber):
    if vendas_a_prazo == 0:
        return "Vendas a prazo não podem ser zero."
    return (contas_a_receber / vendas_a_prazo) * 365


def calcular_periodo_medio_pagamento(compras_a_prazo, contas_a_pagar):
    if compras_a_prazo == 0:
        return "Compras a prazo não podem ser zero."
    return (contas_a_pagar / compras_a_prazo) * 365


def calcular_ciclo_operacional(periodo_medio_recebimento, periodo_medio_estoque):
    return periodo_medio_recebimento + periodo_medio_estoque


# -----------------------------
# Helpers para o menu (entrada segura)
# -----------------------------

def _ler_valor(prompt, tipo=float, permitir_vazio=False):
    # Loop até o usuário digitar um valor válido (ou vazio, se permitido)
    while True:
        entrada = input(prompt)
        if permitir_vazio and entrada.strip() == '':
            return None
        try:
            if tipo == int:
                # Converte float para int quando o usuário passar algo como '3.0'
                return int(float(entrada))
            return tipo(entrada)
        except Exception:
            # Em caso de erro, avisa e repete
            print('Entrada inválida. Tente novamente.')


def _ler_lista(prompt):
    import ast
    # Lê uma linha e tenta aceitar tanto syntax de lista '[1,2]' quanto '1,2,3'
    while True:
        entrada = input(prompt + " (separe por vírgula, ex: 1,2,3)\n> ")
        try:
            # Interpreta como literal Python se começar com [ ou (
            if entrada.strip().startswith('[') or entrada.strip().startswith('('):
                val = ast.literal_eval(entrada)
                if isinstance(val, (list, tuple)):
                    # Converte cada item para float
                    return [float(x) for x in val]
            # Caso contrário, split por vírgula e converte para float
            partes = [p.strip() for p in entrada.split(',') if p.strip()]
            return [float(p) for p in partes]
        except Exception:
            print('Não foi possível interpretar a lista. Tente novamente.')


def _normalizar_submenu(entrada):
    """Normaliza a escolha do submenu retornando a primeira letra/número alfanumérico.

    Isso permite que o usuário digite 'a', 'A', 'a)' ou 'a )' e ainda assim seja
    reconhecido como a opção 'a'. Se a entrada for vazia retorna string vazia.
    """
    if not entrada:
        return ''
    # Procura o primeiro caracter alfanumérico e retorna em minúscula
    import re
    m = re.search(r'[A-Za-z0-9]', entrada)
    if m:
        return m.group(0).lower()
    return entrada.strip().lower()


# -----------------------------
# Função para chamar qualquer função por nome
# -----------------------------

def chamar_funcao_por_nome():
    import ast
    # Pergunta o nome da função ao usuário
    nome = input('Nome da função a chamar (ex: soma, media, calcular_imc): ').strip()
    if nome == '':
        return
    # Busca função no escopo global (deste módulo)
    func = globals().get(nome)
    if not callable(func):
        print('Função não encontrada:', nome)
        return
    # Pergunta ao usuário os argumentos como expressão Python ou lista/tupla
    args_str = input('Argumentos (ex: 1, 2  ou [1,2,3] para lista). Deixe vazio para nenhum argumento:\n> ').strip()
    try:
        if args_str == '':
            args = ()
        else:
            try:
                # Tenta interpretar toda a string como literal Python
                parsed = ast.literal_eval(args_str)
                if isinstance(parsed, tuple):
                    args = parsed
                elif isinstance(parsed, list):
                    # Se for lista, passa a lista como único argumento
                    args = (parsed,)
                else:
                    # Valor único (número, string, etc.)
                    args = (parsed,)
            except Exception:
                # Se literal_eval falhar, divide por vírgulas e interpreta cada parte
                partes = [p.strip() for p in args_str.split(',') if p.strip()]
                parsed_parts = []
                for p in partes:
                    try:
                        parsed_parts.append(ast.literal_eval(p))
                    except Exception:
                        try:
                            parsed_parts.append(float(p))
                        except Exception:
                            parsed_parts.append(p)
                args = tuple(parsed_parts)
        # Chama a função com os argumentos construídos
        resultado = func(*args)
        print('\nResultado:', resultado)
    except Exception as e:
        print('Erro ao executar função:', e)


# -----------------------------
# Menu interativo (interface de texto)
# -----------------------------

def menu_principal():
    # Loop principal do menu; roda até o usuário escolher sair.
    while True:
        print('\n' + '=' * 40)
        print('MENU INTERATIVO - FUNÇÕES MATEMÁTICAS')
        print('1) Operações aritméticas básicas (soma, subtracao, multiplicacao, divisao, potencia)')
        print('2) Funções estatísticas (media, mediana, moda, desvio_padrao)')
        print('3) Trigonometria (seno, cosseno, tangente)')
        print('4) Conversões e utilitários (conversões de unidade, imc)')
        print('5) Geometria (area/volume/hipotenusa)')
        print('6) Física e economia (forca, energia, juros, amortizacao)')
        print('7) Chamar função por nome (entrada livre de argumentos)')
        print('0) Sair')
        escolha = input('Escolha uma opção: ').strip()

        if escolha == '0':
            print('Saindo...')
            break

        if escolha == '1':
            # Lê dois valores (float padrão) e chama operações básicas
            a = _ler_valor('Digite o primeiro número: ')
            b = _ler_valor('Digite o segundo número: ')
            print('soma:', soma(a, b))
            print('subtracao:', subtracao(a, b))
            print('multiplicacao:', multiplicacao(a, b))
            print('divisao:', divisao(a, b))
            print('potencia:', potencia(a, b))

        elif escolha == '2':
            # Lê lista e imprime medidas estatísticas
            lista = _ler_lista('Digite os números')
            print('media:', media(lista))
            print('mediana:', mediana(lista))
            print('moda:', moda(lista))
            print('desvio_padrao:', desvio_padrao(lista))

        elif escolha == '3':
            ang = _ler_valor('Digite o ângulo em graus: ')
            print('seno:', seno(ang))
            print('cosseno:', cosseno(ang))
            print('tangente:', tangente(ang))

        if escolha == '4':
            # Sub-menu para conversões rápidas
            print('a) IMC  b) Quilômetros->Milhas  c) Celsius->Fahrenheit')
            sub = _normalizar_submenu(input('Escolha: '))
            if sub == 'a':
                peso = _ler_valor('Peso (kg): ')
                altura = _ler_valor('Altura (m): ')
                print('IMC:', calcular_imc(peso, altura))
            elif sub == 'b':
                km = _ler_valor('Quilômetros: ')
                print('Milhas:', quilometros_para_milhas(km))
            elif sub == 'c':
                c = _ler_valor('Celsius: ')
                print('Fahrenheit:', celsius_para_fahrenheit(c))
            else:
                print('Opção inválida.')

        elif escolha == '5':
            print('a) Área círculo  b) Área retângulo  c) Volume esfera  d) Hipotenusa')
            sub = _normalizar_submenu(input('Escolha: '))
            if sub == 'a':
                r = _ler_valor('Raio: ')
                print('Área:', calcular_area_circulo(r))
            elif sub == 'b':
                l = _ler_valor('Largura: ')
                h = _ler_valor('Altura: ')
                print('Área:', calcular_area_retangulo(l, h))
            elif sub == 'c':
                r = _ler_valor('Raio: ')
                print('Volume:', calcular_volume_esfera(r))
            elif sub == 'd':
                c1 = _ler_valor('Cateto 1: ')
                c2 = _ler_valor('Cateto 2: ')
                print('Hipotenusa:', hipotenusa(c1, c2))
            else:
                print('Opção inválida.')

        elif escolha == '6':
            print('a) Força  b) Energia cinética  c) Juros simples  d) Amortização (price)')
            sub = _normalizar_submenu(input('Escolha: '))
            if sub == 'a':
                m = _ler_valor('Massa (kg): ')
                acc = _ler_valor('Aceleração (m/s^2): ')
                print('Força:', calcular_forca(m, acc))
            elif sub == 'b':
                m = _ler_valor('Massa (kg): ')
                v = _ler_valor('Velocidade (m/s): ')
                print('Energia cinética:', calcular_energia_cinetica(m, v))
            elif sub == 'c':
                p = _ler_valor('Principal: ')
                taxa = _ler_valor('Taxa (ex: 0.05 para 5%): ')
                t = _ler_valor('Tempo: ')
                print('Juros simples:', calcular_juro_simples(p, taxa, t))
            elif sub == 'd':
                v = _ler_valor('Valor do empréstimo: ')
                taxa = _ler_valor('Taxa por período (ex: 0.01): ')
                n = _ler_valor('Número de parcelas: ', tipo=int)
                print('Parcelas (price):', calcular_amortizacao_price(v, taxa, n))
            else:
                print('Opção inválida.')

        elif escolha == '7':
            # Permite chamar qualquer função do módulo digitando seu nome
            chamar_funcao_por_nome()

        else:
            # Entrada inválida no menu principal
            print('Opção inválida. Tente novamente.')


# Ponto de entrada: roda o menu quando o arquivo é executado diretamente
if __name__ == '__main__':
    try:
        menu_principal()
    except KeyboardInterrupt:
        # Tratamento de CTRL+C para saída limpa
        print('\nInterrompido pelo usuário. Saindo...')
