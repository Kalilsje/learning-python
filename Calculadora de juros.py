Valor = input("Valor do empréstimo: ");
TaxaJuros = int(input("Taxa de Juros: "));
Anos = input("Quantidade de anos: ");
Valor = int(Valor);
TaxaJuros = int(TaxaJuros);
Anos = int(Anos);
Emprestimo = Valor * ((1 + (TaxaJuros/100))**Anos);
print("O valor total que o cliente deverá pagar será de R$ " + str(round(Emprestimo))+ ",00");