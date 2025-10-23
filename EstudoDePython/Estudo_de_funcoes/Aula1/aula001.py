"""Módulo de utilitários matemáticos e menu interativo.

Este arquivo reúne muitas funções pequenas (aritmética, estatística,
geometria, física e finanças) e fornece um menu interativo para
testar/executar rapidamente essas funções.

Cada função tem uma docstring concisa explicando parâmetros e retorno.
"""


# -----------------------------
# Operações aritméticas básicas
# -----------------------------
def soma(a, b):
    """Retorna a + b.

    Args:
        a (float|int): primeiro operando
        b (float|int): segundo operando

    Returns:
        float|int: soma
    """
    return a + b


def subtracao(a, b):
    """Retorna a - b."""
    return a - b


def multiplicacao(a, b):
    """Retorna a * b."""
    return a * b


def divisao(a, b):
    """Retorna a / b; evita divisão por zero.

    Retorna uma mensagem de erro (string) se b == 0.
    """
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."


# -----------------------------
# Potências e radiciação
# -----------------------------
def potencia(a, b):
    """Retorna a ** b (expoente).

    Aceita expoentes não inteiros.
    """
    return a ** b


def raiz_quadrada(a):
    """Retorna raiz quadrada de a se a >= 0, caso contrário retorna mensagem."""
    if a >= 0:
        return a ** 0.5
    else:
        return "Raiz quadrada de número negativo não é permitida."


def raiz_cubica(a):
    """Retorna a raiz cúbica de a."""
    return a ** (1 / 3)


def fatorial(n):
    """Retorna n! para n inteiro >= 0; retorna mensagem para n < 0."""
    if n < 0:
        return "Fatorial de número negativo não é definido."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado


def porcentagem(total, percentual):
    """Calcula (total * percentual) / 100."""
    return (total * percentual) / 100


# -----------------------------
# Logaritmos e trigonometria
# -----------------------------
def logaritmo(a, base=10):
    """Calcula log de 'a' na base especificada; valida entradas."""
    import math

    if a > 0 and base > 1:
        return math.log(a, base)
    else:
        return "Logaritmo indefinido para esses valores."


def seno(angulo):
    """Retorna seno de um ângulo em graus."""
    import math

    return math.sin(math.radians(angulo))


def cosseno(angulo):
    """Retorna cosseno de um ângulo em graus."""
    import math

    return math.cos(math.radians(angulo))


def tangente(angulo):
    """Retorna tangente de um ângulo em graus."""
    import math

    return math.tan(math.radians(angulo))


# -----------------------------
# Utilitários simples
# -----------------------------
def valor_absoluto(a):
    """Retorna o valor absoluto de a."""
    return abs(a)


def arredondar(a, casas_decimais=0):
    """Arredonda 'a' para o número de casas informado (padrão 0)."""
    return round(a, casas_decimais)


def minimo(a, b):
    """Retorna o menor entre a e b."""
    return min(a, b)


def maximo(a, b):
    """Retorna o maior entre a e b."""
    return max(a, b)


# -----------------------------
# Estatística básica
# -----------------------------
def media(lista):
    """Retorna a média aritmética de uma lista; 0 para lista vazia."""
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


def mediana(lista):
    """Retorna a mediana de uma lista de números; 0 para lista vazia."""
    if len(lista) == 0:
        return 0
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2
    if n % 2 == 0:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        return lista_ordenada[meio]


def moda(lista):
    """Retorna uma lista com as modas; None se não houver moda ou lista vazia."""
    from collections import Counter

    if len(lista) == 0:
        return None
    contagem = Counter(lista)
    max_frequencia = max(contagem.values())
    modas = [k for k, v in contagem.items() if v == max_frequencia]
    if len(modas) == len(contagem):
        return None  # Sem moda
    return modas


def desvio_padrao(lista):
    """Calcula o desvio padrão populacional de uma lista (denominador = n)."""
    import math

    if len(lista) == 0:
        return 0
    media_valor = media(lista)
    variancia = sum((x - media_valor) ** 2 for x in lista) / len(lista)
    return math.sqrt(variancia)


def combinacao(n, k):
    """Retorna C(n, k) (combinação) para inteiros não-negativos; 0 se inválido."""
    from math import factorial

    if k > n or n < 0 or k < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def permutacao(n, k):
    """Retorna P(n, k) (permutação) para inteiros não-negativos; 0 se inválido."""
    from math import factorial

    if k > n or n < 0 or k < 0:
        return 0
    return factorial(n) // factorial(n - k)


# -----------------------------
# Geometria básica
# -----------------------------
def hipotenusa(cateto1, cateto2):
    """Calcula a hipotenusa dado os dois catetos (teorema de Pitágoras)."""
    import math

    return math.hypot(cateto1, cateto2)


# -----------------------------
# Conversões de unidades
# -----------------------------
def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9


def quilometros_para_milhas(km):
    """Converte quilômetros para milhas (aprox.)."""
    return km * 0.621371


def milhas_para_quilometros(milhas):
    """Converte milhas para quilômetros (aprox.)."""
    return milhas / 0.621371


def litros_para_galoes(litros):
    """Converte litros para galões (US)."""
    return litros * 0.264172


def galoes_para_litros(galoes):
    """Converte galões (US) para litros."""
    return galoes / 0.264172


def metros_para_pes(metros):
    """Converte metros para pés (aprox.)."""
    return metros * 3.28084


def pes_para_metros(pes):
    """Converte pés para metros (aprox.)."""
    return pes / 3.28084


def segundos_para_horas(segundos):
    """Converte segundos para horas (float)."""
    return segundos / 3600


def horas_para_segundos(horas):
    """Converte horas para segundos."""
    return horas * 3600


def dias_para_semanas(dias):
    """Converte dias para semanas (float)."""
    return dias / 7


def semanas_para_dias(semanas):
    """Converte semanas para dias."""
    return semanas * 7


def anos_para_dias(anos):
    """Converte anos para dias, considerando 365.25 dias por ano (médio)."""
    return anos * 365.25


def dias_para_anos(dias):
    """Converte dias para anos (média com anos bissextos)."""
    return dias / 365.25


# -----------------------------
# Áreas, volumes e utilitários de geometria
# -----------------------------
def calcular_imc(peso, altura):
    """Calcula IMC = peso / (altura ** 2). Valida altura > 0."""
    if altura <= 0:
        return "Altura deve ser maior que zero."
    return peso / (altura ** 2)


def calcular_area_circulo(raio):
    """Retorna área do círculo (π * r^2); valida raio não-negativo."""
    import math

    if raio < 0:
        return "Raio não pode ser negativo."
    return math.pi * (raio ** 2)


def calcular_area_retangulo(largura, altura):
    """Retorna área do retângulo; valida dimensões não-negativas."""
    if largura < 0 or altura < 0:
        return "Largura e altura não podem ser negativas."
    return largura * altura


def calcular_area_triangulo(base, altura):
    """Retorna área do triângulo (base * altura / 2); valida entradas."""
    if base < 0 or altura < 0:
        return "Base e altura não podem ser negativas."
    return (base * altura) / 2


def calcular_volume_esfera(raio):
    """Retorna volume da esfera (4/3 * π * r^3); valida entrada."""
    import math

    if raio < 0:
        return "Raio não pode ser negativo."
    return (4 / 3) * math.pi * (raio ** 3)


def calcular_volume_cilindro(raio, altura):
    """Retorna volume do cilindro (π * r^2 * h); valida entradas."""
    import math

    if raio < 0 or altura < 0:
        return "Raio e altura não podem ser negativos."
    return math.pi * (raio ** 2) * altura


def calcular_volume_cone(raio, altura):
    """Retorna volume do cone (1/3 * π * r^2 * h); valida entradas."""
    import math

    if raio < 0 or altura < 0:
        return "Raio e altura não podem ser negativos."
    return (1 / 3) * math.pi * (raio ** 2) * altura


# -----------------------------
# Física básica: distância, velocidade, forças, energia
# -----------------------------
def calcular_distancia_pontos(x1, y1, x2, y2):
    """Calcula distância euclidiana entre dois pontos 2D."""
    import math

    return math.hypot(x2 - x1, y2 - y1)


def calcular_velocidade(distancia, tempo):
    """Retorna velocidade média = distancia / tempo; valida tempo > 0."""
    if tempo <= 0:
        return "Tempo deve ser maior que zero."
    return distancia / tempo


def calcular_aceleracao(velocidade_inicial, velocidade_final, tempo):
    """Retorna aceleração média = (vf - vi) / tempo; valida tempo > 0."""
    if tempo <= 0:
        return "Tempo deve ser maior que zero."
    return (velocidade_final - velocidade_inicial) / tempo


def calcular_forca(massa, aceleracao):
    """Retorna força = massa * aceleração (Segunda Lei de Newton)."""
    return massa * aceleracao


def calcular_trabalho(forca, deslocamento):
    """Retorna trabalho = força * deslocamento (quando força paralela ao deslocamento)."""
    return forca * deslocamento


def calcular_energia_cinetica(massa, velocidade):
    """Retorna energia cinética = 0.5 * m * v^2."""
    return 0.5 * massa * (velocidade ** 2)


def calcular_energia_potencial(massa, altura, gravidade=9.81):
    """Retorna energia potencial gravitacional = m * g * h."""
    return massa * gravidade * altura


def calcular_pressao(forca, area):
    """Retorna pressão = força / área; valida área > 0."""
    if area <= 0:
        return "Área deve ser maior que zero."
    return forca / area


def calcular_densidade(massa, volume):
    """Retorna densidade = massa / volume; valida volume > 0."""
    if volume <= 0:
        return "Volume deve ser maior que zero."
    return massa / volume


# -----------------------------
# Ondas e ângulos (funções trigonométricas inversas auxiliares)
# -----------------------------
def calcular_frequencia(tempo_periodo):
    """Retorna frequência = 1 / período; valida período > 0."""
    if tempo_periodo <= 0:
        return "Tempo do período deve ser maior que zero."
    return 1 / tempo_periodo


def calcular_periodo(frequencia):
    """Retorna período = 1 / frequência; valida frequência > 0."""
    if frequencia <= 0:
        return "Frequência deve ser maior que zero."
    return 1 / frequencia


def calcular_angulo_seno(oposto, hipotenusa):
    """Retorna o ângulo (em graus) cujo seno = oposto/hipotenusa.

    Valida hipotenusa != 0 e razão entre -1 e 1.
    """
    if hipotenusa == 0:
        return "Hipotenusa não pode ser zero."
    import math

    seno_valor = oposto / hipotenusa
    if seno_valor < -1 or seno_valor > 1:
        return "Valor de seno inválido."
    return math.degrees(math.asin(seno_valor))


def calcular_angulo_cosseno(adjacent, hipotenusa):
    """Retorna o ângulo (em graus) cujo cosseno = adjacent/hipotenusa."""
    if hipotenusa == 0:
        return "Hipotenusa não pode ser zero."
    import math

    cosseno_valor = adjacent / hipotenusa
    if cosseno_valor < -1 or cosseno_valor > 1:
        return "Valor de cosseno inválido."
    return math.degrees(math.acos(cosseno_valor))


def calcular_angulo_tangente(oposto, adjacent):
    """Retorna o ângulo (em graus) cuja tangente = oposto/adjacent; valida adjacent != 0."""
    if adjacent == 0:
        return "Adjacente não pode ser zero."
    import math

    return math.degrees(math.atan(oposto / adjacent))


def calcular_media_ponderada(valores, pesos):
    """Retorna média ponderada dados valores e pesos; valida entradas."""
    if len(valores) != len(pesos) or len(valores) == 0:
        return "Listas de valores e pesos devem ter o mesmo tamanho e não podem ser vazias."
    soma_ponderada = sum(v * p for v, p in zip(valores, pesos))
    soma_pesos = sum(pesos)
    if soma_pesos == 0:
        return "A soma dos pesos não pode ser zero."
    return soma_ponderada / soma_pesos


# -----------------------------
# Finanças básicas
# -----------------------------
def calcular_juro_simples(principal, taxa, tempo):
    """Retorna juros simples = principal * taxa * tempo."""
    return principal * taxa * tempo


def calcular_juro_composto(principal, taxa, tempo):
    """Retorna juros compostos acumulados (montante - principal)."""
    return principal * ((1 + taxa) ** tempo - 1)


def calcular_valor_futuro(principal, taxa, tempo):
    """Retorna montante futuro = principal * (1 + taxa) ** tempo."""
    return principal * (1 + taxa) ** tempo


def calcular_valor_presente(valor_futuro, taxa, tempo):
    """Desconta valor futuro para o presente com taxa composta."""
    return valor_futuro / (1 + taxa) ** tempo


def calcular_taxa_crescimento(valor_inicial, valor_final, tempo):
    """Calcula taxa média anual de crescimento (composta)."""
    if valor_inicial <= 0 or tempo <= 0:
        return "Valor inicial e tempo devem ser maiores que zero."
    return (valor_final / valor_inicial) ** (1 / tempo) - 1


def calcular_taxa_desconto(valor_futuro, valor_presente, tempo):
    """Calcula taxa de desconto implícita entre presente e futuro."""
    if valor_presente <= 0 or tempo <= 0:
        return "Valor presente e tempo devem ser maiores que zero."
    return (valor_futuro / valor_presente) ** (1 / tempo) - 1


def calcular_amortizacao_sac(valor_emprestimo, taxa_juros, numero_parcelas):
    """Calcula tabela SAC: amortização constante mais juros decrescentes."""
    if numero_parcelas <= 0:
        return "Número de parcelas deve ser maior que zero."
    amortizacao = valor_emprestimo / numero_parcelas
    saldo_devedor = valor_emprestimo
    parcelas = []
    for i in range(numero_parcelas):
        juros = saldo_devedor * taxa_juros
        parcela = amortizacao + juros
        parcelas.append(parcela)
        saldo_devedor -= amortizacao
    return parcelas


def calcular_amortizacao_price(valor_emprestimo, taxa_juros, numero_parcelas):
    """Calcula parcelas no sistema Price (prestações constantes)."""
    if numero_parcelas <= 0 or taxa_juros < 0:
        return "Número de parcelas deve ser maior que zero e taxa de juros não pode ser negativa."
    fator = (taxa_juros * (1 + taxa_juros) ** numero_parcelas) / ((1 + taxa_juros) ** numero_parcelas - 1)
    parcela = valor_emprestimo * fator
    return [parcela] * numero_parcelas


def calcular_taxa_efetiva_anual(taxa_nominal, periodos):
    """Converte taxa nominal para taxa efetiva anual com 'periodos' períodos por ano."""
    if periodos <= 0:
        return "Número de períodos deve ser maior que zero."
    return (1 + taxa_nominal / periodos) ** periodos - 1


def calcular_taxa_nominal(taxa_efetiva, periodos):
    """Calcula taxa nominal dada a taxa efetiva anual e número de períodos."""
    if periodos <= 0:
        return "Número de períodos deve ser maior que zero."
    return periodos * ((1 + taxa_efetiva) ** (1 / periodos) - 1)


def calcular_valor_presente_liquido(fluxos_caixa, taxa_desconto):
    """Calcula VPL dado uma lista de fluxos de caixa e taxa de desconto."""
    vpl = 0
    for t, fluxo in enumerate(fluxos_caixa):
        vpl += fluxo / (1 + taxa_desconto) ** t
    return vpl


def calcular_taxa_interna_retorno(fluxos_caixa, estimativa_inicial=0.1, tolerancia=1e-6, max_iteracoes=1000):
    """Estima a TIR usando método de Newton-Raphson; retorna None se não convergir."""
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
    """Calcula ponto de equilíbrio em unidades (custos_fixos / (preco - custo_var))."""
    if preco_venda <= custo_variavel:
        return "Preço de venda deve ser maior que custo variável."
    return custos_fixos / (preco_venda - custo_variavel)


def calcular_marketing_roi(receita, custo_marketing):
    """Calcula ROI de marketing: (receita - custo) / custo; valida custo != 0."""
    if custo_marketing == 0:
        return "Custo de marketing não pode ser zero."
    return (receita - custo_marketing) / custo_marketing


def calcular_lucro_bruto(receita, custo_vendas):
    """Retorna lucro bruto = receita - custo de vendas."""
    return receita - custo_vendas


def calcular_lucro_liquido(receita, custos_totais, despesas):
    """Retorna lucro líquido = receita - custos_totais - despesas."""
    return receita - custos_totais - despesas


def calcular_margem_lucro_bruto(lucro_bruto, receita):
    """Retorna margem de lucro bruto (lucro_bruto / receita); valida receita != 0."""
    if receita == 0:
        return "Receita não pode ser zero."
    return lucro_bruto / receita


def calcular_margem_lucro_liquido(lucro_liquido, receita):
    """Retorna margem de lucro líquido (lucro_liquido / receita); valida receita != 0."""
    if receita == 0:
        return "Receita não pode ser zero."
    return lucro_liquido / receita


def calcular_roa(lucro_liquido, ativos_totais):
    """Return on Assets: lucro_liquido / ativos_totais; valida ativos_totais != 0."""
    if ativos_totais == 0:
        return "Ativos totais não podem ser zero."
    return lucro_liquido / ativos_totais


def calcular_roe(lucro_liquido, patrimonio_liquido):
    """Return on Equity: lucro_liquido / patrimonio_liquido; valida != 0."""
    if patrimonio_liquido == 0:
        return "Patrimônio líquido não pode ser zero."
    return lucro_liquido / patrimonio_liquido


def calcular_current_ratio(ativos_circulantes, passivos_circulantes):
    """Current ratio = ativos_circulantes / passivos_circulantes; valida != 0."""
    if passivos_circulantes == 0:
        return "Passivos circulantes não podem ser zero."
    return ativos_circulantes / passivos_circulantes


def calcular_quick_ratio(ativos_circulantes, estoques, passivos_circulantes):
    """Quick ratio = (ativos_circulantes - estoques) / passivos_circulantes; valida != 0."""
    if passivos_circulantes == 0:
        return "Passivos circulantes não podem ser zero."
    return (ativos_circulantes - estoques) / passivos_circulantes


def calcular_giro_ativos(receita, ativos_totais):
    """Giro dos ativos = receita / ativos_totais; valida != 0."""
    if ativos_totais == 0:
        return "Ativos totais não podem ser zero."
    return receita / ativos_totais


def calcular_giro_estoques(custo_vendas, estoque_medio):
    """Giro de estoques = custo_vendas / estoque_medio; valida != 0."""
    if estoque_medio == 0:
        return "Estoque médio não pode ser zero."
    return custo_vendas / estoque_medio


def calcular_periodo_medio_recebimento(vendas_a_prazo, contas_a_receber):
    """Período médio de recebimento em dias; valida vendas a prazo != 0."""
    if vendas_a_prazo == 0:
        return "Vendas a prazo não podem ser zero."
    return (contas_a_receber / vendas_a_prazo) * 365


def calcular_periodo_medio_pagamento(compras_a_prazo, contas_a_pagar):
    """Período médio de pagamento em dias; valida compras a prazo != 0."""
    if compras_a_prazo == 0:
        return "Compras a prazo não podem ser zero."
    return (contas_a_pagar / compras_a_prazo) * 365


def calcular_ciclo_operacional(periodo_medio_recebimento, periodo_medio_estoque):
    """Retorna soma dos dois períodos médios (ciclo operacional)."""
    return periodo_medio_recebimento + periodo_medio_estoque



def _ler_valor(prompt, tipo=float, permitir_vazio=False):
    """Auxiliar de entrada: lê e converte para 'tipo'; repete em caso de erro."""
    while True:
        entrada = input(prompt)
        if permitir_vazio and entrada.strip() == '':
            return None
        try:
            if tipo == int:
                return int(float(entrada))
            return tipo(entrada)
        except Exception:
            print('Entrada inválida. Tente novamente.')


def _ler_lista(prompt):
    """Lê uma linha e tenta interpretar como lista (ou separação por vírgula).

    Retorna uma lista de floats.
    """
    import ast

    while True:
        entrada = input(prompt + " (separe por vírgula, ex: 1,2,3)\n> ")
        try:
            # Tenta interpretar como lista literal primeiro
            if entrada.strip().startswith('[') or entrada.strip().startswith('('):
                val = ast.literal_eval(entrada)
                if isinstance(val, (list, tuple)):
                    return [float(x) for x in val]
            # Caso contrário, separa por vírgula
            partes = [p.strip() for p in entrada.split(',') if p.strip()]
            return [float(p) for p in partes]
        except Exception:
            print('Não foi possível interpretar a lista. Tente novamente.')


def chamar_funcao_por_nome():
    """Permite ao usuário chamar qualquer função definida neste módulo pelo nome.

    O usuário informa o nome da função e os argumentos (como expressão Python).
    """
    import ast

    nome = input('Nome da função a chamar (ex: soma, media, calcular_imc): ').strip()
    if nome == '':
        return
    func = globals().get(nome)
    if not callable(func):
        print('Função não encontrada:', nome)
        return
    args_str = input('Argumentos (ex: 1, 2  ou [1,2,3] para lista). Deixe vazio para nenhum argumento:\n> ').strip()
    try:
        if args_str == '':
            args = ()
        else:
            # Tenta interpretar como uma expressão Python (lista, tupla, números)
            try:
                parsed = ast.literal_eval(args_str)
                if isinstance(parsed, tuple):
                    args = parsed
                elif isinstance(parsed, list):
                    # passar a lista inteira como um único argumento
                    args = (parsed,)
                else:
                    # número único
                    args = (parsed,)
            except Exception:
                # fallback: dividir por vírgula
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
        resultado = func(*args)
        print('\nResultado:', resultado)
    except Exception as e:
        print('Erro ao executar função:', e)


def menu_principal():
    """Menu interativo que agrupa e chama várias funções do módulo."""
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
            a = _ler_valor('Digite o primeiro número: ')
            b = _ler_valor('Digite o segundo número: ')
            print('soma:', soma(a, b))
            print('subtracao:', subtracao(a, b))
            print('multiplicacao:', multiplicacao(a, b))
            print('divisao:', divisao(a, b))
            print('potencia:', potencia(a, b))

        elif escolha == '2':
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

        elif escolha == '4':
            print('a) IMC  b) Quilômetros->Milhas  c) Celsius->Fahrenheit')
            sub = input('Escolha: ').strip().lower()
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
            sub = input('Escolha: ').strip().lower()
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
            sub = input('Escolha: ').strip().lower()
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
            chamar_funcao_por_nome()

        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    try:
        menu_principal()
    except KeyboardInterrupt:
        print('\nInterrompido pelo usuário. Saindo...')

