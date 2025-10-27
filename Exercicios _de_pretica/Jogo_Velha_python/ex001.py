

def mostrar_tabuleiro(tabuleiro):

    for lina in tabuleiro:

        print(' | '.join(lina))
        print('--+---+--')

def verificar_vitoria(tabuleiro, jogador):
    
    for _ in range(3):
        # verificar linhas
        if tabuleiro[_][0] == jogador and tabuleiro[_][1] == jogador and tabuleiro[_][2] == jogador:
            return True
    for _ in range(3):
        # Verificando colunas
        if tabuleiro[0][_] == jogador and tabuleiro[1][_] == jogador and tabuleiro[2][_] == jogador:
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] ==jogador and tabuleiro [2][0] == jogador:
        return True

    return False

tabuleiro = [['1','2','3'],
             ['4','5','6'],
             ['7','8','9']]

jogador_atual = 'X'

for rodada in range(9):

    mostrar_tabuleiro(tabuleiro)

    escolha = input(f'Jogador {jogador_atual}, escolha uma posição de (1-9): ')

    try:
        posicao = int(escolha) -1
        linha, coluna = posicao // 3, posicao % 3


        if tabuleiro[linha][coluna] in ['X', 'O']:

            print('Posição já ocupada. Tente outra posição!')

            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)

            print(f'Jogador {jogador_atual} Venceu!!!!!!')

            break

        if jogador_atual == 'O':
            jogador_atual = 'X'
        else:
            jogador_atual = 'O'

    except ValueError:

        print('Erro... Muitas tentativas invalidas!')
        break
        

    