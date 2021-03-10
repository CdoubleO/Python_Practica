'''
TP7
'''
def cifrar(msj):
    cfrMedio = ''
    cfrFinal = ''
    n = 0
    for i in range(len(msj)):
        if msj[i].lower() in 'aeiou':
            x = msj[i-n:i]
            x = x[::-1] + msj[i]
            cfrMedio += x
            n = 0
        elif i == len(msj)-1:
            x = msj[i:i-n-1:-1]
            cfrMedio += x          
        else:
            n += 1
    l =  len(cfrMedio)
    for i in range((l//2)):
        x = cfrMedio[i] + cfrMedio[l-1-i]
        cfrFinal += x
    if l % 2 == 1:
        cfrFinal += cfrMedio[(l//2)]
    print(f'{msj} => {cfrMedio} => {cfrFinal}')
    return cfrFinal


def descifrar(cfr):
    dcfrMedio = ['','','']
    dcfrFinal = ''
    msj = ''
    l =  len(cfr)
    if l % 2 == 1:
        msj = cfr[:l-1]
        dcfrMedio[1] += cfr[-1]
        l -= 1
    else:
        msj = cfr
    for i in range(0,l,2):
        dcfrMedio[0] += msj[i]
        dcfrMedio[2] += msj[i+1]
    dcfrMedio = dcfrMedio[0]+dcfrMedio[1]+dcfrMedio[2][::-1]
    n = 0
    for i in range(len(dcfrMedio)):
        if dcfrMedio[i].lower() in 'aeiou':
            x = dcfrMedio[i-n:i]
            x = x[::-1] + dcfrMedio[i]
            dcfrFinal += x
            n = 0
        elif i == len(dcfrMedio)-1:
            x = dcfrMedio[i:i-n-1:-1]
            dcfrFinal += x          
        else:
            n += 1
    return f'{dcfrMedio} => {dcfrFinal}'


msj = 'En un lugar de la Mancha...'
cfr = cifrar(msj)
# print(f'{msj} => {cfr}')
dcfr = descifrar(cfr)
print(f'{cfr} => {dcfr}')