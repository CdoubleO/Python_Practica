'''
TP1
1) Generar un mazo de cartas españolas al azar, se entiende por mazo de cartas a un
conjunto de 48 cartas no ordenadas y almacenarlas en una pila de cartas.
(Pista: investigar el tipo de datos set para obtener las 48 cartas sin repeticiones)
2) A continuación se pide programar el siguiente juego:
Repartir una carta a cada uno de 4 jugadores formando así una mano, gana la mano el
jugador que tenía la carta de mayor valor. El premio del ganador de la mano es
acumular las cartas de la mano en su propia pila, es decir, que cada jugador poseerá
una pila de cartas inicialmente en estado vacío. Repetir este proceso hasta que no
queden cartas en el mazo. Gana el juego el jugador cuya pila de cartas tenga
acumulado el mayor valor sumando el valor numérico de todas las cartas que se
encuentran en su pila. Si hay dos o más jugadores con igual suma se tendrá en cuenta
la cantidad de manos ganadas para desempatar el juego.
'''
from random import randint


def generarCarta():
    '''Devuelve una tupla conformada por el valor de carta (1 a 12) y el palo'''
    palo = ('O','B','C','E')
    return (randint(1,12),palo[randint(0,3)])


def generarMazo():
    ''' Devuelve un mazo que es un set con 48 tuplas'''
    mazo = set()
    while len(mazo) < 48:
        mazo.add(generarCarta())
    return mazo


def repartirCarta(mazo):
    '''saca el ultimo item del set mazo y lo devuelve, es una tupla'''
    return mazo.pop()


def generarManos(mazo):
    ''' genera una lista con cuatr cartas(tuplas) cada una pertenece a un jugador distinto'''
    manos = []
    while len(manos) < 4:
        manos.append(repartirCarta(mazo))
    return manos


def cartaMayor(manos):
    '''Devulve indice de jugador que gana'''
    cMayor = 0
    j = 0 
    for i in range(4):
        # como no dice que pasa si hay dos valores iguales en la mano gana el primero que se registra
        if cMayor < manos[i][0]:
            cMayor = manos[i][0]
            j = i
    return j


def ganadorFinal(jgds,contMG):
    sumas = {'1': 0,'2': 0,'3': 0,'4': 0}
    for j in jgds:
        suma = 0
        for t in jgds[j]:
            suma += t[0]
        sumas[j] = suma
    maxi = 0
    i = ''
    for j in sumas:
        if maxi < sumas[j]:
            maxi = sumas[j]
            i = j
        elif maxi == sumas[j]:
            if contMG[i] < contMG[j]:
                i = j 
    # print(sumas)
    return i


def juegoCartas():
    jgds = {'1': [],'2': [],'3': [],'4': []}
    mazo = generarMazo()
    contMG = {'1': 0,'2': 0,'3': 0,'4': 0}
    while len(mazo) > 0:
        manos = generarManos(mazo)
        ganaMano = str(cartaMayor(manos)+1)
        contMG[ganaMano] += 1   
        jgds[ganaMano].extend(manos)
    print('El ganador es el jugador {}'.format(ganadorFinal(jgds, contMG)))
    # print(contMG)


juegoCartas()

