def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("Denominador não pode ser zero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        divisor = mdc(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor
        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1

    def add(self, outra):
        novo_numerador = self.numerador * outra.denominador + outra.numerador * self.denominador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def sub(self, outra):
        novo_numerador = self.numerador * outra.denominador - outra.numerador * self.denominador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def mult(self, outra):
        novo_numerador = self.numerador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def div(self, outra):
        if outra.numerador == 0:
            raise ValueError("Não é possível dividir por uma fração com numerador zero.")
        novo_numerador = self.numerador * outra.denominador
        novo_denominador = self.denominador * outra.numerador
        return Fracao(novo_numerador, novo_denominador)

    def to_float(self):
        return self.numerador / self.denominador

    def to_string(self):
        return f"( {self.numerador} / {self.denominador} )"

    def compares_to(self, outra):
        a = self.numerador * outra.denominador
        b = outra.numerador * self.denominador
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0