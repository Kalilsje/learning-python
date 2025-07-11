LadoA = input("Tamanho do primeiro lado: ");
LadoB = input("Tamanho do segundo lado: ");
LadoC = input("Tamanho do terceiro lado: ");
LadoA = int(LadoA)
LadoB = int(LadoB)
LadoC = int(LadoC)

if LadoA < (LadoB + LadoC) or LadoB < (LadoA + LadoC) or LadoC < (LadoA + LadoB):
    if LadoA == LadoB == LadoC:
        print("É um triângulo equilátero");
    elif LadoA != LadoB != LadoC:
        print("É um triângulo escaleno");
    else:
        print("É um triângulo isósceles");