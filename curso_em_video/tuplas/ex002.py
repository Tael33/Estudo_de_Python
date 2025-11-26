# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time do Botafogo.

times = ("Flamengo",
    "Palmeiras",
    "Cruzeiro",
    "Mirassol",
    "Botafogo",
    "Bahia",
    "Fluminense",
    "São Paulo",
    "Red Bull Bragantino",
    "Corinthians",
    "Atlético-MG",
    "Grêmio",
    "Vasco da Gama",
    "Ceará",
    "Internacional",
    "Vitória",
    "Santos",
    "Fortaleza",
    "Juventude",
    "Sport"
    )

print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 4 útimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O Botafogo está na {times.index('Botafogo')+1}ª posição')