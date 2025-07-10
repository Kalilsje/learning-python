Lados = 0
LadoA = input("Tamanho do primeiro lado: ");
LadoB = input("Tamanho do segundo lado: ");
LadoC = input("Tamanho do terceiro lado: ");
LadoA = int(LadoA)
LadoB = int(LadoB)
LadoC = int(LadoC)
Lados = int(Lados)

if LadoA < (LadoB + LadoC):
    print("É um triângulo");
else:
    print("Não é um triângulo");

if LadoB < (LadoA + LadoC):
    print("É um triângulo");
else:
    print("Não é um triângulo");

if LadoC < (LadoA + LadoB):
    print("É um triângulo");
else:
    print("Não é um triângulo");

if LadoA == LadoB == LadoC:
    print("É um triângulo equilátero");
elif LadoA != LadoB != LadoC:
    print("É um triângulo escaleno");
else:
    print("É um triângulo isósceles");