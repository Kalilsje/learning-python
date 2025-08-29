def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tabuleiro):
    print()
    for i in range(3):
        linha = ""
        for j in range(3):
            posicao = i * 3 + j + 1
            valor = tabuleiro[i][j] if tabuleiro[i][j] != " " else str(posicao)
            linha += f" {valor} "
            if j < 2:
                linha += "|"
        print(linha)
        if i < 2:
            print("---+---+---")
    print()

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def tabuleiro_cheio(tabuleiro):
    return all(tabuleiro[i][j] != " " for i in range(3) for j in range(3))

def obter_posicao(numero):
    numero -= 1  
    linha = numero // 3
    coluna = numero % 3
    return linha, coluna

def jogar():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    while True:
        mostrar_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")

        try:
            escolha = int(input("Escolha uma posição (1-9): "))
            if escolha < 1 or escolha > 9:
                print("Posição inválida! Escolha de 1 a 9.\n")
                continue
        except ValueError:
            print("Entrada inválida! Digite um número de 1 a 9.\n")
            continue

        linha, coluna = obter_posicao(escolha)

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada. Tente outra.\n")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!\n")
            break

        if tabuleiro_cheio(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("Empate! O tabuleiro está cheio.\n")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

jogar()