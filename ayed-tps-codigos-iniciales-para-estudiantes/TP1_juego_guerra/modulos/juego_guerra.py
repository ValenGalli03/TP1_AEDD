import random
from Cartas import Carta, Mazo
from Cola_D import Cola

class JuegoGuerra:
    def __init__(self):
        self.mazo_jugador1 = Mazo()
        self.mazo_jugador2 = Mazo()
        self.mesa = Cola()
        self.turno = 0

    def inicializar_mazos(self):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        palos = ['♠', '♥', '♦', '♣']
        mazo_completo = [Carta(valor, palo) for valor in valores for palo in palos]
        self.mazo_jugador1.cartas = random.sample(mazo_completo, 26)
        self.mazo_jugador2.cartas = [carta for carta in mazo_completo if carta not in self.mazo_jugador1.cartas]

    def jugar(self):
        self.inicializar_mazos()
        self.mazo_jugador1.barajar()
        self.mazo_jugador2.barajar()

        while self.turno < 10000:
            self.turno += 1
            print(f"turno:{self.turno}")

            carta_jugador1 = self.mazo_jugador1.sacar_carta()
            carta_jugador2 = self.mazo_jugador2.sacar_carta()
            self.mesa.agregar(carta_jugador1)
            self.mesa.agregar(carta_jugador2)

            # Imprimir las cartas jugadas en este turno
            print(f"Jugador 1: {carta_jugador1}")
            print(f"Jugador 2: {carta_jugador2}")


         # Verificar si uno de los jugadores se quedó sin cartas
            if not self.mazo_jugador1.cartas:
              print("*** Jugador 2 GANA LA PARTIDA ***")
              break
            elif not self.mazo_jugador2.cartas:
                print("*** Jugador 1 GANA LA PARTIDA ***")
                break

            if carta_jugador1.valor == carta_jugador2.valor:
                print("¡Guerra!")

                # Implementar el manejo de "Guerra" aquí
                while True:
                  for _ in range(3):
                        carta_jugador1 = self.mazo_jugador1.sacar_carta()
                        carta_jugador2 = self.mazo_jugador2.sacar_carta()
                        self.mesa.agregar(carta_jugador1)
                        self.mesa.agregar(carta_jugador2)

                        carta_jugador1 = self.mazo_jugador1.sacar_carta()
                        carta_jugador2 = self.mazo_jugador2.sacar_carta()
                        self.mesa.agregar(carta_jugador1)
                        self.mesa.agregar(carta_jugador2)

                        print(f"Jugador 1 (Guerra): {carta_jugador1}")
                        print(f"Jugador 2 (Guerra): {carta_jugador2}")
                  if carta_jugador1.valor != carta_jugador2.valor:
                   if carta_jugador1.valor > carta_jugador2.valor:
                      self.mazo_jugador1.cartas.extend(list(self.mesa))
                      self.mesa = Cola()
                      print("Jugador 1 gana la Guerra")
                  else:
                    self.mazo_jugador2.cartas.extend(list(self.mesa))
                    self.mesa = Cola()
                    print("Jugador 2 gana la Guerra")
                  break
        
            else:
                if  carta_jugador1.valor > carta_jugador2.valor:
                    self.mazo_jugador1.cartas.extend(list(self.mesa))
                    self.mesa = Cola()
                    print("Jugador 1 gana el turno")
                else:
                    self.mazo_jugador2.cartas.extend(list(self.mesa))
                    self.mesa = Cola()
                    print("Jugador 2 gana el turno")

            # Verificar si se llegó a un empate después de 10,000 turnos
            if self.turno == 10000:
                print("*** EMPATE ***")
                break

if __name__ == "__main__":
    juego = JuegoGuerra()
    juego.jugar()


