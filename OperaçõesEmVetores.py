entrada1 = input("Digite os elementos do vetor A, separados por espaço: ")
vetor1 = list(map(int, entrada1.split()))

entrada2 = input("Digite os elementos do vetor B, separados por espaço: ")
vetor2 = list(map(int, entrada2.split()))

conjunto1 = set(vetor1)
conjunto2 = set(vetor2)

uniao = list(conjunto1.union(conjunto2))

diferenca1e2 = list(conjunto1.difference(conjunto2))

diferenca2e1 = list(conjunto2.difference(conjunto1))

intersecao = list(conjunto1.intersection(conjunto2))

print("\nResultado das operações entre os vetores A e B:")
print(f"União: {uniao}")
print(f"Diferença A - B: {diferenca1e2}")
print(f"Diferença B - A: {diferenca2e1}")
print(f"Interseção: {intersecao}")