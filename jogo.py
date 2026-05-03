import random

# Variável global de dificuldade
dificuldade = "dificil"


def verificar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for c in combinacoes:
        if all(tabuleiro[i] == jogador for i in c):
            return True
    return False


def empate(tabuleiro):
    return "" not in tabuleiro


def jogada_aleatoria(tabuleiro):
    livres = [i for i in range(9) if tabuleiro[i] == ""]
    return random.choice(livres)


def minimax(tabuleiro, profundidade, is_max):
    if verificar_vitoria(tabuleiro, "O"):
        return 1
    if verificar_vitoria(tabuleiro, "X"):
        return -1
    if empate(tabuleiro):
        return 0

    if is_max:
        melhor = -float("inf")
        for i in range(9):
            if tabuleiro[i] == "":
                tabuleiro[i] = "O"
                score = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = ""
                melhor = max(melhor, score)
        return melhor
    else:
        melhor = float("inf")
        for i in range(9):
            if tabuleiro[i] == "":
                tabuleiro[i] = "X"
                score = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = ""
                melhor = min(melhor, score)
        return melhor


def melhor_jogada(tabuleiro):
    melhor_valor = -float("inf")
    melhor_mov = None

    for i in range(9):
        if tabuleiro[i] == "":
            tabuleiro[i] = "O"
            valor = minimax(tabuleiro, 0, False)
            tabuleiro[i] = ""

            if valor > melhor_valor:
                melhor_valor = valor
                melhor_mov = i

    return melhor_mov


def jogada_maquina(tabuleiro):
    global dificuldade

    if dificuldade == "facil":
        return jogada_aleatoria(tabuleiro)

    elif dificuldade == "medio":
        if random.random() < 0.5:
            return jogada_aleatoria(tabuleiro)
        else:
            return melhor_jogada(tabuleiro)

    else:  # dificil
        return melhor_jogada(tabuleiro)