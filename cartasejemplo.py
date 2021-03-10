import random


def generarCarta():
    palos = ("B","E","O","C")
    valor_carta = random.randint(1,12)
    palo_carta = random.choice(palos)
    boca_abajo = True
    carta = (valor_carta, palo_carta, boca_abajo)
    return carta


def generarMazo():
    mazo = set()
    while len(mazo) < 48:
       mazo.add(generarCarta())
    return mazo


def mezclarMazo():
    pass



print (generarMazo())
