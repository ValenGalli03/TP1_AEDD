import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor}{self.palo}"

class Mazo:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def sacar_carta(self):
        if not self.cartas:
            return None
        return self.cartas.pop(0)

    def barajar(self):
        random.shuffle(self.cartas)