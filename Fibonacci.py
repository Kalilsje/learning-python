numero = int(input("Digite um número positivo: "))
a = 1
b = 1
print(a, end=" ")
print(b, end=" ")
while True:
    proximo = a + b  

    if proximo > numero:
        break

    print(proximo, end=" ")

    a = b
    b = proximo