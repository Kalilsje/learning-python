n = int(input("Fatorial de: "))
if n < 0:
    print("Não tem fatorial")
else:
    f = 1
    for i in range(1, n + 1):
        f *= i
        print(f"o fatorial de {n} é {f}.");