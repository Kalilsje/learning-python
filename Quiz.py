pontuacao = 0
Opcao = input("Qual arma é vendida a 2700 no lado TR do CS?\n" "a) M4A4\n"  "b) FAMAS\n" "c) Ak-47\n" "d) M4A1-S\n");
if Opcao == "c":
    print("Resposta Certa")
    pontuacao =+ 1
else:
    print("Resposta Errada")


Escolha = input("Qual skin é da raridade exótica no CS?\n" "a) Dragon Lore\n"  "b) Howl\n" "c) Medusa\n" "d) Fire Serpent\n");
if Escolha == "b":
    print("Resposta Certa")
    pontuacao =+ 2
else:
    print("Resposta Errada")


Decisao = input("Qual Caixa se dropa a Fire Serpent no CS? \n" "a) Bravo\n"  "b) Revolver\n" "c) Hydra\n" "d) Aperto\n");
if Decisao == "a":
    print("Resposta Certa")
    pontuacao =+ 3
else:
    print("Resposta Errada")

print("Sua pontuacao final foi de: ", pontuacao);