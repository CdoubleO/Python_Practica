'''
TP4
'''
tabla = [
    ['', 'A','B','C','D','E'],
    ['A','a','b','c','d','e'],
    ['B','f','g','h',('i','j'),'k'],
    ['C','l','m',('n','ñ'),'o','p'],
    ['D','q','r','s','t','u'],
    ['E','v','w','x','y','z']
]

def cifrar(msj):
    cfr = ''
    for l in msj.lower():
        if l == ' ':
            cfr += l
        else:
            for f in range(len(tabla)):
                for c in range(len(tabla[f])):
                    if l in tabla[f][c]:
                        xx = tabla[f][0] + tabla[0][c]
                        cfr += xx            
    return cfr


def descifrar(cfr):
    dcfr = ''
    for p in cfr.split(' '):
        for i in range(0,len(p),2):
            i2 = tabla[0].index(p[i+1])
            for f in range(len(tabla)):
                if p[i] == tabla[f][0]:
                    if len(tabla[f][i2]) > 1:
                        dcfr += '('
                        for x in tabla[f][i2]: 
                            dcfr += x
                        dcfr += ')'
                    else:
                        dcfr += tabla[f][i2]            
        dcfr += ' '
    return dcfr.strip(' ')


msj = input('Ingrese mensaje a cifrar: ')
# msj = 'deseamos la paz'
cfr = cifrar(msj)
print('Mensaje Cifrado: ' + cfr)
dcfr = descifrar(cfr)
print('Mensaje Descifrado: ' + dcfr)

'''
variante
'''
tabla2 = [
    ['', '1','2','3','4','5'],
    ['1','a','b','c','d','e'],
    ['2','f','g','h',('i','j'),'k'],
    ['3','l','m',('n','ñ'),'o','p'],
    ['4','q','r','s','t','u'],
    ['5','v','w','x','y','z']
]

def cifrar2(msj):
    cfr = ''
    for l in msj.lower():
        if l == ' ':
            cfr += l
        else:
            for f in range(len(tabla2)):
                for c in range(len(tabla2[f])):
                    if l in tabla2[f][c]:
                        xx = tabla2[f][0] + tabla2[0][c]
                        cfr += xx            
    return cfr


def descifrar2(cfr):
    dcfr = ''
    for p in cfr.split(' '):
        for i in range(0,len(p),2):
            i2 = tabla2[0].index(p[i+1])
            for f in range(len(tabla2)):
                if p[i] == tabla2[f][0]:
                    if len(tabla2[f][i2]) > 1:
                        dcfr += '('
                        for x in tabla2[f][i2]: 
                            dcfr += x
                        dcfr += ')'
                    else:
                        dcfr += tabla2[f][i2]            
        dcfr += ' '
    return dcfr.strip(' ')


cfr2 = cifrar2(msj)
print('Mensaje Cifrado: ' + cfr2)
dcfr2 = descifrar2(cfr2)
print('Mensaje Descifrado: ' + dcfr2)