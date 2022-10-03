class Carta:
    def __init__(self) -> None:
        self.cartas = {1: ['12T', '5R', '6C', '11E', '10C', '2E', '3T', '11R', '2R', '12E'], 2: ['2T', '4T', '13T', '7T', '6T', '7R', '3C', '3R', '13R', '1R'] }



class PilaDeCartas(Carta):

    def __init__(self) -> None:
        super().__init__(self.cartas)
        self.cartas = self.cartas
    def apilar(self, t):
        turno = 1
        pila = []
        while True:
            actual = pila[-1] if len(pila) > 0 else ''
            palo = actual[-1] if actual else False
            numero = actual[0:-1] if actual else False
            if len(self.cartas[t]) == 0:
                print('El jugador {} no tiene más cartas'.format(t))
                break
            carta_a_jugar = self.cartas[t][0]
            if carta_a_jugar[-1] == palo or carta_a_jugar[0:-1] == numero or not actual:
                pila.append(carta_a_jugar)
                print(pila)
                self.cartas[t].pop(0)
            else:
                raise ValueError('No se puede jugar la carta {} del jugador {} sobre la carta {}'.format(
                    carta_a_jugar, t, actual)
                )
            t = 2 if t == 1 else 1

    def __str__(self):
        return(self.apilar)


cartas = Carta
pila = PilaDeCartas
pila.apilar()