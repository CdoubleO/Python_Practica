'''
Hacer algoritmos para detectar las figuras del poker.
ej: full, pares
valores: 1,2,3,4,5,6,7,8,9,10,11,12,13
palos: t,d,c,p
'''
import random as r

def generarMazo():
    palo = ['P','C','T','D']
    mazo = set()
    while len(mazo) < 52:
        nro = r.randint(1,13)
        p = palo[r.randint(0,3)]
        mazo.add((nro,p))
    return mazo


def generarMano(mazo):
    mazo = list(mazo)
    mano = []
    for i in range(5):
        c = mazo.pop(i)
        mano.append(c)

    return set(mano)


def esPar(mano):
    contadores = [0]*14 #[00000000000000]
    for v,p in mano:
        contadores[v] += 1
    return contadores.count(2)  == 1


def esParDoble(mano):
    contadores = [0]*14 #[00000000000000]
    for v,p in mano:
        contadores[v] += 1
    return contadores.count(2)  == 2


def esTrio(mano):
    contadores = [0]*14 #[00000000000000]
    for v,p in mano:
        contadores[v] += 1
    return contadores.count(3)  == 1


def esFull(mano):
    contadores = [0]*14 #[00000000000000]
    for v,p in mano:
        contadores[v] += 1
    return contadores.count(3)  == 1 and contadores.count(2) == 1


def esEscalera(mano):
    contadores = [0]*14
    flag = False
    for v,p in mano:
        contadores[v] += 1
    if contadores.count(1) == 5:
        for i in range(len(contadores)):
            if contadores[i] == 1 and contadores[i:i+5].count(1) == 5:
                flag = True
                return flag
    return flag


def esColor(mano):
    contadores = dict()
    flag = False
    for v,p in mano:
        if p in contadores:
            contadores[p] += 1
        else:
            contadores[p] = 1 
    for k in contadores:
        if contadores[k] == 5:
            flag = True
            return flag
    return flag


def esEscaleraColor(mano):
    if esColor(mano) and esEscalera(mano):
        return True
    return False


def esPoker(mano):
    contadores = [0]*14
    for v,p in mano:
        contadores[v] += 1
    return contadores.count(4) == 1


def cartaAlta(mano):
    n = 0
    for v,p in mano:
        if n < v:
            n = v
            carta = (v,p)
    return {carta}


def check(mano):
    if esFull(mano):
        return 'Full'
    elif esParDoble(mano):
        return 'Par Doble'
    elif esPar(mano):
        return 'Par'
    elif esTrio(mano):
        return 'Trío'
    elif esEscalera(mano):
        if esEscaleraColor(mano):
            return 'Escalera de color'
        else:
            return 'Escalera'
    elif esPoker(mano):
        return 'Poker'
    elif esColor(mano):
        return 'Color'
    else:
        return cartaAlta(mano)


def app():
    mano = {(1, 'p'), (1,'d'),(1,'c'),(1,'t'),(5,'p')}
    # mazo = generarMazo()
    # mano = generarMano(mazo)
    forma = check(mano)
    print(mano)
    if type(forma) == str:
        print(forma)
    else:
        print(f'Carta Alta: {forma}')


# Corre la funcion
app()

