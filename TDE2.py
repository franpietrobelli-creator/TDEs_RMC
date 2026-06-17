#  TDE 2 — Jogo de Labirinto em Grade

#  Regras do Jogo:
#  - O jogador (J) começa no canto superior esquerdo
#  - O objetivo é encontrar e chegar até a saída (S)
#  - '#' = parede  |  '.' = espaço livre  |  '?' = fumaça
#  - O jogador só enxerga as casas próximas dele
#  - Movimente-se com: W (cima), S (baixo), A (esquerda), D (direita)
#  - Digite 'sair' ou '0' para encerrar a qualquer momento
# Bom Jogo!

TABULEIRO = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '#', '.', '#'],
    ['#', '#', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
]

LINHA_INICIO = 1
COL_INICIO   = 1
LINHA_SAIDA  = 6
COL_SAIDA    = 6


def exibir_com_neblina(tabuleiro, lj, cj):
    """Exibe o tabuleiro, mas oculta tudo que não está ao redor do jogador."""
    linhas  = len(tabuleiro)
    colunas = len(tabuleiro[0])

    print()
    for i in range(linhas):
        linha_str = ""
        for j in range(colunas):
            dist_linha = abs(i - lj)
            dist_col   = abs(j - cj)

            if dist_linha <= 1 and dist_col <= 1:
                if i == lj and j == cj:
                    linha_str += " J"
                else:
                    linha_str += " " + tabuleiro[i][j]
            else:
                linha_str += " ?"

        print(linha_str)
    print()


def mover(lj, cj, direcao):
    if direcao == 'w':
        return lj - 1, cj
    elif direcao == 's':
        return lj + 1, cj
    elif direcao == 'a':
        return lj, cj - 1
    elif direcao == 'd':
        return lj, cj + 1
    return lj, cj


def posicao_valida(tabuleiro, lj, cj):
    linhas  = len(tabuleiro)
    colunas = len(tabuleiro[0])
    if lj < 0 or lj >= linhas or cj < 0 or cj >= colunas:
        return False
    if tabuleiro[lj][cj] == '#':
        return False
    return True


def jogar():
    tabuleiro = [linha[:] for linha in TABULEIRO]
    tabuleiro[LINHA_SAIDA][COL_SAIDA] = 'S'

    lj = LINHA_INICIO
    cj = COL_INICIO

    print("=" * 40)
    print("       Bem-vindo ao Labirinto!")
    print("=" * 40)
    print("  W = cima   S = baixo")
    print("  A = esquerda   D = direita")
    print("  '0' ou 'sair' para encerrar")
    print("  Encontre a saida (S) na neblina...")
    print("=" * 40)

    while True:
        exibir_com_neblina(tabuleiro, lj, cj)

        entrada = input("Movimento: ").strip().lower()

        if entrada in ('0', 'sair'):
            print("\nVoce encerrou o jogo. Ate a proxima!")
            break

        if entrada not in ('w', 'a', 's', 'd'):
            print("Entrada invalida! Use W, A, S ou D.")
            continue

        nova_linha, nova_col = mover(lj, cj, entrada)

        if not posicao_valida(tabuleiro, nova_linha, nova_col):
            print("Movimento bloqueado! Ha uma parede ou limite ali.")
            continue

        lj = nova_linha
        cj = nova_col

        if lj == LINHA_SAIDA and cj == COL_SAIDA:
            exibir_com_neblina(tabuleiro, lj, cj)
            print("=" * 40)
            print("  Parabens! Voce encontrou a saida!")
            print("=" * 40)
            break


jogar()