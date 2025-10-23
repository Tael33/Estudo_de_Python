# ============================================================
# 🧠 TUDO SOBRE DICIONÁRIOS EM PYTHON
# ============================================================
# Dicionário é uma estrutura de dados que armazena pares "chave: valor".
# As chaves devem ser únicas e imutáveis (strings, números, tuplas, etc).
# Os valores podem ser de qualquer tipo.
# ============================================================


# ============================================================
# 🔹 1. CRIAÇÃO DE DICIONÁRIOS
# ============================================================

# Forma 1: Usando chaves {}
dicionario = {"nome": "Maria", "idade": 25, "cidade": "São Paulo"}
print("Dicionário inicial:", dicionario)

# Forma 2: Usando o construtor dict()
dicionario2 = dict(nome="João", idade=30)
print("Usando dict():", dicionario2)

# Forma 3: Criando um dicionário vazio
vazio = {}
print("Dicionário vazio:", vazio)


# ============================================================
# 🔹 2. ACESSAR ELEMENTOS
# ============================================================

print("\nNome:", dicionario["nome"])  # acessa valor diretamente
# print(dicionario["telefone"])  # Erro se não existir

# Usando get() — evita erro se a chave não existir
print("Telefone:", dicionario.get("telefone", "Não encontrado"))


# ============================================================
# 🔹 3. ADICIONAR E ALTERAR ELEMENTOS
# ============================================================

dicionario["profissao"] = "Engenheira"  # adiciona nova chave
dicionario["idade"] = 26                # altera valor existente
print("\nApós adição e alteração:", dicionario)


# ============================================================
# 🔹 4. REMOVER ELEMENTOS
# ============================================================

# del -> remove pela chave
del dicionario["cidade"]

# pop() -> remove e retorna o valor
profissao = dicionario.pop("profissao")
print("Profissão removida:", profissao)

# popitem() -> remove o último item
ultimo = dicionario.popitem()
print("Removido com popitem():", ultimo)

print("Dicionário após remoções:", dicionario)


# ============================================================
# 🔹 5. VERIFICAÇÕES
# ============================================================

print("\nExiste 'nome'? ->", "nome" in dicionario)
print("Existe 'idade'? ->", "idade" in dicionario)
print("Tamanho:", len(dicionario))


# ============================================================
# 🔹 6. ITERAR (PERCORRER) DICIONÁRIO
# ============================================================

dicionario = {"nome": "Ana", "idade": 22, "curso": "Python"}

print("\nChaves:")
for chave in dicionario.keys():
    print(chave)

print("\nValores:")
for valor in dicionario.values():
    print(valor)

print("\nItens (chave e valor):")
for chave, valor in dicionario.items():
    print(f"{chave} -> {valor}")


# ============================================================
# 🔹 7. MÉTODOS ÚTEIS
# ============================================================

dic_exemplo = {"a": 1, "b": 2, "c": 3}

print("\nCópia:", dic_exemplo.copy())

# Atualizar com outro dicionário
dic_exemplo.update({"d": 4, "a": 100})
print("Após update():", dic_exemplo)

# Limpar tudo
dic_exemplo.clear()
print("Após clear():", dic_exemplo)


# ============================================================
# 🔹 8. DICIONÁRIOS ANINHADOS (DENTRO DE DICIONÁRIOS)
# ============================================================

pessoas = {
    "pessoa1": {"nome": "Lucas", "idade": 30},
    "pessoa2": {"nome": "Carla", "idade": 25}
}

print("\nIdade da pessoa1:", pessoas["pessoa1"]["idade"])

# Percorrendo dicionário aninhado
for id, dados in pessoas.items():
    print(f"{id} -> Nome: {dados['nome']}, Idade: {dados['idade']}")


# ============================================================
# 🔹 9. DICIONÁRIO COM LISTAS
# ============================================================

aluno = {
    "nome": "Pedro",
    "notas": [8, 9, 10]
}

media = sum(aluno["notas"]) / len(aluno["notas"])
print("\nMédia do aluno:", media)

# Percorrendo
for nota in aluno["notas"]:
    print("Nota:", nota)


# ============================================================
# 🔹 10. DICIONÁRIOS + LISTAS DE DICIONÁRIOS
# ============================================================

turma = [
    {"nome": "Ana", "nota": 9},
    {"nome": "Carlos", "nota": 7},
    {"nome": "Bruna", "nota": 10}
]

print("\nNotas da turma:")
for aluno in turma:
    print(f"{aluno['nome']} tirou {aluno['nota']}")


# ============================================================
# 🔹 11. DICIONÁRIOS COM TUPLAS
# ============================================================

pontos = {
    "A": (10, 20),
    "B": (30, 40)
}

print("\nCoordenada de A:", pontos["A"][0], pontos["A"][1])

for nome, coordenadas in pontos.items():
    x, y = coordenadas
    print(f"Ponto {nome} está em ({x}, {y})")


# ============================================================
# 🔹 12. DICIONÁRIOS COM CONJUNTOS (SETS)
# ============================================================

dados = {
    "categorias": {"Python", "IA", "Automação"}
}

print("\nCategorias:")
for categoria in dados["categorias"]:
    print(categoria)


# ============================================================
# 🔹 13. COMBINAÇÕES COMPLEXAS
# ============================================================

empresa = {
    "departamentos": [
        {
            "nome": "TI",
            "funcionarios": [
                {"nome": "Rafa", "cargo": "Dev"},
                {"nome": "Bia", "cargo": "Analista"}
            ]
        },
        {
            "nome": "RH",
            "funcionarios": [
                {"nome": "Carlos", "cargo": "Recrutador"}
            ]
        }
    ]
}

print("\nFuncionários da empresa:")
for dep in empresa["departamentos"]:
    print(f"\nDepartamento: {dep['nome']}")
    for func in dep["funcionarios"]:
        print(f" - {func['nome']} ({func['cargo']})")


# ============================================================
# 🔹 14. EXEMPLOS PRÁTICOS (APLICAÇÕES REAIS)
# ============================================================

# Exemplo 1: Contar frequência de palavras em um texto
texto = "python é incrível e python é poderoso"
frequencia = {}
for palavra in texto.split():
    frequencia[palavra] = frequencia.get(palavra, 0) + 1
print("\nFrequência de palavras:", frequencia)

# Exemplo 2: Dicionário de estoque
estoque = {"banana": 10, "maçã": 5, "laranja": 8}
produto = "banana"
if produto in estoque:
    estoque[produto] -= 1
print("Estoque atualizado:", estoque)

# Exemplo 3: Menu de cadastro de usuários
usuarios = {}
usuarios["user1"] = {"nome": "João", "email": "joao@email.com"}
usuarios["user2"] = {"nome": "Maria", "email": "maria@email.com"}
print("\nUsuários cadastrados:")
for id, info in usuarios.items():
    print(f"{id}: {info['nome']} ({info['email']})")


# ============================================================
# 🔹 15. CONVERSÕES E FUNÇÕES ÚTEIS
# ============================================================

# Converter listas em dicionário
chaves = ["a", "b", "c"]
valores = [1, 2, 3]
d = dict(zip(chaves, valores))
print("\nDicionário criado com zip():", d)

# Criar dicionário com valores padrão
padrao = dict.fromkeys(["x", "y", "z"], 0)
print("Dicionário com valores padrão:", padrao)

# Iterar com enumerate()
for i, (k, v) in enumerate(d.items()):
    print(f"{i} -> {k}:{v}")

# ============================================================
# 🔹 16. RESUMO GERAL (CONCEITOS)
# ============================================================
"""
📘 CONCEITOS:
- Dicionário: estrutura que armazena pares chave-valor.
- Chave: identificador único e imutável.
- Valor: qualquer tipo de dado (mutável ou não).
- Métodos úteis: keys(), values(), items(), get(), pop(), update(), clear(), copy(), fromkeys().
- Usos comuns: contadores, cadastros, dados aninhados (JSON), bancos de dados simples.

✅ Dicionário é um dos tipos mais poderosos do Python!
"""
