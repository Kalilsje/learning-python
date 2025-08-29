expressao = input("Digite a expressão com parênteses: ")

pilha = []

for caractere in expressao:
    if caractere == '(':  
        pilha.append('(')
    elif caractere == ')':  
        if len(pilha) > 0:
            pilha.pop()  
        else:
            print("Erro! Parêntese fechado sem ter sido aberto.")
            break

else:
    if len(pilha) == 0:
        print("Expressão OK! Todos os parênteses estão corretos.")
    else:
        print("Erro! Existem parênteses abertos que não foram fechados.")