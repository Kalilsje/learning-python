while True:
    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    operacao = input("Digite o número da operação desejada: ")

    if operacao == "0":
        print("Saindo da calculadora. Tchau!")
        break

    if operacao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        continue

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Você deve digitar um número válido.")
        continue  

    if operacao == "1":
        resultado = numero1 + numero2
        print("Resultado da soma:", resultado)

    elif operacao == "2":
        resultado = numero1 - numero2
        print("Resultado da subtração:", resultado)

    elif operacao == "3":
        resultado = numero1 * numero2
        print("Resultado da multiplicação:", resultado)

    elif operacao == "4":
        if numero2 == 0:
            print("Erro: Não é possível dividir por zero.")
        else:
            resultado = numero1 / numero2
            print("Resultado da divisão:", resultado)