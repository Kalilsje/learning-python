def desenhar_forca(erros):
    fases = [
        "",  
        "|",  
        "|\n|  (_)",  
        "|\n|  (_)\n|   |",  
        "|\n|  (_)\n|   |\n|   |",  
        "|\n|  (_)\n|  \|/\n|   |",  
        "|\n|  (_)\n|  \|/\n|   |\n|  /", 
        "|\n|  (_)\n|  \|/\n|   |\n|  / \\", 
    ]
    print(fases[erros])

palavra_secreta = input("Digite a palavra secreta: ").lower()

print("\n" * 50)

letras_descobertas = ["_" for letra in palavra_secreta]
letras_erradas = []
max_erros = 7
erros = 0

while erros < max_erros and "_" in letras_descobertas:
    print("Palavra: ", " ".join(letras_descobertas))
    print(f"Erros ({erros}/{max_erros}):", " ".join(letras_erradas))
    desenhar_forca(erros)

    tentativa = input("Digite uma letra: ").lower()

    if tentativa in letras_descobertas or tentativa in letras_erradas:
        print("Você já tentou essa letra. Tente outra.\n")
        continue

    if tentativa in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == tentativa:
                letras_descobertas[i] = tentativa
        print("Boa! Você acertou uma letra!\n")
    else:
        erros += 1
        letras_erradas.append(tentativa)
        print("Ops! Letra errada.\n")

if "_" not in letras_descobertas:
    print("\nParabéns! Você descobriu a palavra:", palavra_secreta)
else:
    desenhar_forca(erros)
    print("\nVocê perdeu! A palavra era:", palavra_secreta)