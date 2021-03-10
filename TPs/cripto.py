'''
TP3

'''
alpha = [['a','b','c','d','e','f','g','h','i','j','k','l','m'],
        ['Z','Y','X','W','V','U','T','S','R','Q','P','O','N'],
        ['n','o','p','q','r','s','t','u','v','w','x','y','z'],
        ['M','L','K','J','I','H','G','F','E','D','C','B','A']]

def cifrar(msj):
    cfr = ''
    for l in msj.lower():
        if l in alpha[0]:
            cfr += alpha[1][alpha[0].index(l)] 
        elif l in alpha[2]:
            cfr += alpha[3][alpha[2].index(l)]
        else:
            cfr += l
    return cfr


def descifrar(cfr):
    dcfr = ''
    for l in cfr:
        if l in alpha[1]:
            dcfr += alpha[0][alpha[1].index(l)] 
        elif l in alpha[3]:
            dcfr += alpha[2][alpha[3].index(l)]
        else:
            dcfr += l
    return dcfr 


msj = input('Ingrese mensaje a cifrar: ')
cfr = cifrar(msj)
print(cfr)
dcfr = descifrar(cfr)
print(dcfr)