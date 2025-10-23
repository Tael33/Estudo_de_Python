# Guia completo e detalhado: `aula001_fully_annotated.py`

Este documento é uma versão ampliada e detalhada do material de apoio para o arquivo
`aula001_fully_annotated.py`. O objetivo é explicar, de forma didática e completa,
para que serve cada parte do código, como usar cada função, uma definição clara das
construções ("tags") do Python que aparecem no arquivo, e exemplos práticos.

Se você está aprendendo, leia este arquivo devagar e experimente os exemplos no
seu REPL ou executando o script. Sempre que quiser, peça para eu comentar linha-a-linha
um bloco específico e eu farei.

---

Sumário rápido (o que contém este guia)

- Visão geral do projeto e propósito do arquivo Python
- Como executar e testar localmente
- Explicação detalhada das bibliotecas usadas (por que, funções principais, exemplos)
- Glossário exaustivo das construções do Python usadas no código (def, return, if, for, etc.)
- Documentação de cada função do módulo (assinatura, parâmetros, retornos, comportamentos de erro e exemplos)
- Boas práticas e alternativas sugeridas (Type Hints, docstrings padrão, exceções)
- Exercícios práticos para consolidar o aprendizado
- Próximos passos — como posso ajudar a continuar

---

1) Visão geral do arquivo Python

- Propósito: fornecer um conjunto de funções utilitárias matemáticas e científicas
  e um menu interativo para usar essas funções sem escrever código adicional.
- Organização: o arquivo está dividido em blocos temáticos (aritmética, trigonometria,
  estatística, conversões, geometria, física, finanças), helpers de entrada, uma
  função que permite chamar outras funções por nome e o `menu_principal()`.
- Uso típico: executar o script com `python aula001_fully_annotated.py` para abrir
  o menu interativo; ou importar funções específicas para uso em outros scripts.

Exemplo rápido (executar no terminal/powershell):

```powershell
& "H:\programação\EstudoDePython\curso_em_video\.venv\Scripts\python.exe" "h:/programação/EstudoDePython/curso_em_video/modulo1/Aula1/aula001_fully_annotated.py"
```

---

2) Como testar e desenvolver localmente

- Recomendo usar um virtualenv (parece que você já tem `.venv` no projeto). Para ativar no PowerShell:

```powershell
# Ativar virtualenv (Windows PowerShell)
& "H:\programação\EstudoDePython\curso_em_video\.venv\Scripts\Activate.ps1"

# Ou executar diretamente o python do virtualenv
& "H:\programação\EstudoDePython\curso_em_video\.venv\Scripts\python.exe" "modulo1/Aula1/aula001_fully_annotated.py"
```

- Checar sintaxe (rápido):

```powershell
& "H:\programação\EstudoDePython\curso_em_video\.venv\Scripts\python.exe" -m py_compile "modulo1/Aula1/aula001_fully_annotated.py"
```

- Rodar testes manuais: execute funções no REPL, ex.:

```python
from modulo1.Aula1.aula001_fully_annotated import soma, media
print(soma(2, 3))
print(media([1,2,3]))
```

---

3) Bibliotecas e módulos usados — explicado em detalhe

A seguir explico cada módulo da biblioteca padrão usado no código, para que serve,
como é usado no arquivo e exemplos práticos.

3.1 `math` — matemática de alto desempenho

- Para que serve: fornece constantes e funções matemáticas implementadas em C, com
  alta precisão e desempenho.
- Porque foi escolhida: oferece funções como `pi`, `sin`, `cos`, `tan`, `hypot`,
  `radians`/`degrees`, `sqrt`, que são padrões para cálculos trigonométricos e
  geométricos.
- Onde aparece no código: trigonometria, áreas e volumes, hipotenusa, conversões
  entre graus e radianos, funções de raiz.
- Funções-chave e exemplos:
  - `math.pi` — valor de π: `math.pi` ≈ 3.14159
  - `math.hypot(x, y)` — calcula sqrt(x*x + y*y) com robustez numérica (evita overflow em algumas situações)
  - `math.radians(deg)` / `math.degrees(rad)` — converte entre graus e radianos
  - `math.sin(x)`, `math.cos(x)`, `math.tan(x)` — recebem radianos
  - `math.asin(x)`, `math.acos(x)`, `math.atan(x)` — funções inversas (retornam radianos)

Exemplo:

```python
import math
math.sin(math.radians(30))  # -> 0.5
math.hypot(3, 4)  # -> 5.0
math.pi * 2  # -> 6.283...
```

Boas práticas:
- Em módulos grandes, prefira `import math` no topo do arquivo em vez de importar repetidamente dentro de funções.

3.2 `collections.Counter` — contagem de elementos

- Para que serve: contador eficiente de ocorrências de elementos em iteráveis.
- Uso no código: calcular moda (elementos mais frequentes) de uma lista.
- Exemplo:

```python
from collections import Counter
c = Counter(["a", "b", "a"])  # Counter({'a': 2, 'b': 1})
c.most_common(1)  # -> [('a', 2)]
```

Boas práticas:
- `Counter` é preferível a criar dicionários manualmente para contar frequências.

3.3 `ast.literal_eval` — parse seguro de literais Python

- Para que serve: interpreta strings contendo literais Python (`'[1,2,3]'`, `'(1,2)'`, `"3"`) e as converte em objetos Python sem executar código arbitrário.
- Por que `literal_eval` e não `eval`: `eval` executa qualquer código Python e representa risco de segurança se o usuário puder fornecer a string; `literal_eval` só interpreta literais.
- Uso no código: permitir ao usuário digitar uma lista, tupla ou número de forma textual e transformá-la num objeto Python.

Exemplo:

```python
import ast
ast.literal_eval('[1,2,3]')  # -> [1, 2, 3]
ast.literal_eval('3')  # -> 3
```

3.4 `re` — expressões regulares (regex)

- Para que serve: localizar padrões em strings.
- Uso no código: `_normalizar_submenu` extrai o primeiro caractere alfanumérico digitado pelo usuário (assim `a)` vira `a`).
- Exemplo básico:

```python
import re
m = re.search(r'[A-Za-z0-9]', 'a)')
print(m.group(0))  # 'a'
```

---

4) Glossário detalhado: cada construção do Python usada no código

Abaixo você encontra explicações e exemplos de cada keyword / construção que aparece no arquivo.

4.1 `def name(params):` — definir função

- O que faz: cria um objeto função que pode ser chamado posteriormente.
- Parâmetros podem ter valores default, serem nomeados, etc.
- Exemplo:

```python
def soma(a, b=0):
    return a + b
```

4.2 `return` — devolver valor

- Termina a execução da função e retorna o valor especificado ao chamador.
- Sem `return`, a função retorna `None`.

4.3 `if/elif/else` — condicional

- Permite executar blocos diferentes dependendo da condição booleana.
- Exemplo:

```python
if x < 0:
    print('negativo')
elif x == 0:
    print('zero')
else:
    print('positivo')
```

4.4 `for` e `while` — laços

- `for i in range(n)` itera sobre uma sequência (lista, tupla, range, etc.).
- `while cond:` repete até `cond` ser falso.
- `break` interrompe o loop; `continue` salta para a próxima iteração.

4.5 `try/except` — tratamento de exceções

- Bloco para capturar erros esperados e evitar que o programa quebre.
- É boa prática capturar exceções específicas (ex.: `except ValueError:`) ao invés de `except Exception:` genérico.
- `finally` (não usado no arquivo) executa código independentemente se houve exceção.

Exemplo:

```python
try:
    x = int(input('Número: '))
except ValueError:
    print('Entrada inválida')
```

4.6 `import` / `from ... import ...` — incluir módulos

- `import math` importa todo o módulo e exige `math.func()` para acessar.
- `from math import pi` importa apenas `pi` para o escopo local.
- `as` permite renomear (`import numpy as np`).

4.7 `isinstance(obj, type)` — checagem de tipos

- Retorna True se `obj` for instância de `type`.
- Exemplo: `isinstance([1,2], list)` -> True.

4.8 `globals()` e execução dinâmica

- `globals()` retorna dicionário do escopo global do módulo. Útil para obter uma função a partir do seu nome (string).
- Risco: executar dinamicamente funções por nome pode ser perigoso se o nome vier de input não confiável.

4.9 `__name__ == '__main__'`

- Permite que o código rode ações (ex.: menu) somente quando o arquivo é executado diretamente, não quando importado.

4.10 Expressões geradoras e comprehensions

- Exemplo de expressão geradora: `sum((x - m) ** 2 for x in lista)` — cria um iterador e calcula soma sem criar lista temporária.
- Comprehension de lista: `[x*x for x in range(10)]` — sintaxe compacta para construir listas.

4.11 Tipos básicos e conversões

- `int()`, `float()`, `str()` convertem entre tipos.
- `int(float('3.0'))` é usado no helper `_ler_valor` para aceitar entradas como `3.0` quando `tipo=int`.

---

5) Documentação pormenorizada de cada função

Abaixo cada função é descrita com: assinatura, para que serve, parâmetros, retorno, exemplos e comentários de borda. Esta seção é extensa — leia por bloco.

Nota: adaptei e escrevi descrições didáticas; use-as como referência quando escrever testes.


---

Bloco: Operações Aritméticas

`def soma(a, b)`
- Propósito: soma dois valores numéricos (ou concatena strings se ambos forem strings).
- Parâmetros: `a` (int|float|str), `b` (int|float|str)
- Retorno: soma ou concatenação.
- Exemplo: `soma(1,2) -> 3`, `soma('a','b') -> 'ab'`.
- Observação: não faz validação de tipos; se quiser garantir números, verifique com `isinstance`.

`def subtracao(a, b)` — subtrai `b` de `a`.

`def multiplicacao(a, b)` — retorna `a * b`.

`def divisao(a, b)`
- Se `b == 0` retorna mensagem de erro. Alternativa mais robusta:

```python
if b == 0:
    raise ZeroDivisionError('Divisor não pode ser zero')
return a / b
```


---

Bloco: Potências e raízes

`def potencia(a, b)` — `a ** b`.

`def raiz_quadrada(a)`
- Se `a < 0`, retorna string de erro. Alternativa: levantar `ValueError`.

`def raiz_cubica(a)`
- Para números negativos, `a ** (1/3)` em ponto flutuante pode produzir número complexo em alguns contextos; solução segura:

```python
import math
def raiz_cubica_real(a):
    return math.copysign(abs(a) ** (1/3), a)
```

`def fatorial(n)`
- Implementação iterativa para evitar profundidade de recursão.
- Entradas inválidas (n < 0) retornam string; alternativa: `raise ValueError`.

---

Bloco: Estatística (média, mediana, moda, desvio)

`def media(lista)`
- Se `lista` vazia retorna 0. Alternativa: lançar `ValueError` para forçar tratamento pelo chamador.

`def mediana(lista)`
- Ordena e retorna o elemento do meio; se par, média dos dois do meio.

`def moda(lista)`
- Usa `Counter` para contar ocorrências e retorna lista de modas quando houver mais de uma.
- Se todas as frequências são iguais (ex.: [1,2,3]) retorna `None` (interpretação do autor: sem moda).

`def desvio_padrao(lista)`
- Fórmula populacional: divide por `n`. Para amostral substitua divisor por `n-1`.

---

Bloco: Combinação e Permutação

`def combinacao(n, k)`
- Retorna número de combinações (n choose k) usando factorial e validações básicas.
- Observação: para grandes `n` use `math.comb` (Python 3.8+) que é mais eficiente.

`def permutacao(n, k)`
- Observação: Python 3.8+ tem `math.perm`.

---

Bloco: Trigonometria

- As funções recebem ângulo em graus (mais intuitivo para iniciantes) e convertem para radianos com `math.radians`.
- Ex.: `seno(30) == 0.5`.
- Atenção: `math.tan(90°)` é indefinido (tende ao infinito); em floats resulta em número grande ou lançar exceção dependendo do input.

---

Bloco: Conversões de unidades e utilitários

- Funções diretas (quilômetros <-> milhas, litros <-> galões, metros <-> pés) usam fatores constantes; são fáceis de testar.
- `calcular_imc(peso, altura)` valida `altura > 0` para evitar divisão por zero.

---

Bloco: Geometria (áreas e volumes)

- Verifique sempre entradas negativas (raio < 0) e retorne/lançe erro adequado.
- Fórmulas clássicas: círculo (πr²), volume esfera (4/3 π r^3), cilindro (π r² h).

---

Bloco: Física e utilitários físicos

- Fórmulas diretas com validação de denominadores (tempo > 0, área > 0, volume > 0).
- Use unidades consistentes (metros, segundos, kg) para não misturar sistemas.

---

Bloco: Finanças

- Juros simples: `principal * taxa * tempo`.
- Juros compostos: `principal * ((1 + taxa) ** tempo - 1)` retorna somente os juros acumulados; `valor_futuro` retorna o montante.
- Amortização Price e SAC implementadas; verifique se a taxa está na unidade correta (por período) e se `numero_parcelas` > 0.
- VPL e TIR: TIR implementada por Newton-Raphson; para maior robustez usar bibliotecas financeiras ou bracketing + bisection se Newton não convergir.

---

6) Segurança e considerações de design

- Input de usuário: sempre validar e sanitizar. O uso de `ast.literal_eval` é uma boa prática comparado a `eval`.
- Execução dinâmica (`globals().get(nome)`): perigosa se exposta a usuários externos. Para produção, crie um dicionário de funções permitidas.

Exemplo seguro:

```python
funcoes_permitidas = {'soma': soma, 'media': media}
nome = input('Nome da função: ')
func = funcoes_permitidas.get(nome)
if func:
    func(...)
else:
    print('Função não permitida')
```

- Erros: prefira lançar exceções (`ValueError`, `ZeroDivisionError`) em bibliotecas; trate as exceções na interface (menu) para mostrar mensagens amigáveis.

---

7) Boas práticas para evoluir o código

- Adicionar Type Hints (PEP 484) e docstrings padronizadas (PEP 257).
- Escrever testes unitários com `pytest`.
- Exportar funções úteis para um pacote (estruturar em `src/` ou `package/`) e escrever README com instruções de uso.
- Considere dividir o arquivo em módulos menores (ex.: `aritmetica.py`, `estatistica.py`, `geometria.py`) para melhor manutenibilidade.

Exemplo de docstring com Type Hints:

```python
def calcular_imc(peso: float, altura: float) -> float:
    """Calcula o Índice de Massa Corporal (IMC).

    Args:
        peso: massa em quilogramas.
        altura: altura em metros.

    Returns:
        IMC calculado (float).

    Raises:
        ValueError: se altura <= 0.
    """
    if altura <= 0:
        raise ValueError('Altura deve ser maior que zero')
    return peso / (altura ** 2)
```

---

8) Exercícios práticos (para praticar)

1. Converter funções que retornam string de erro para lançar exceções adequadas; atualizar o `menu_principal` para capturar e mostrar mensagens amigáveis.
2. Adicionar Type Hints e usar `mypy` para checar tipos.
3. Escrever testes com `pytest` cobrindo casos normais e de borda.
4. Refatorar o menu para separar UI (entrada/saída) da lógica (funções puras) e possívelmente criar uma versão com interface gráfica simples (Tkinter) como exercício.
5. Implementar um dicionário `funcoes_permitidas` para substituir `globals()` e evitar execução arbitrária.

---

9) Próximos passos que eu posso executar para você

- Gerar docstrings com Type Hints para todas as funções automaticamente.
- Comentar linha-a-linha um bloco (sugestão: começar pelas primeiras 10 funções), colocando explicações em português explicando cada linha.
- Criar um conjunto de testes `tests/test_aula001.py` com `pytest` e rodar localmente.
- Empacotar com PyInstaller para gerar `.exe` (usarei o Python do seu virtualenv se preferir).

Diga qual desses itens prefere que eu execute agora e eu vou fazê-lo (executarei as operações diretamente no workspace e validarei com testes/compilações rápidas).

---

Se desejar que eu comece imediatamente a comentar por linha, diga "comentar por linhas" e qual bloco prefere que eu inicie (ex.: "aritmética" ou "estatística").