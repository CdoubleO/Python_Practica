'''
TP6
'''
def comprimirImg(imagen):
    compr = ''
    n = 1
    for l in range(1,len(imagen)):
        if imagen[l] == imagen[l-1]:
            n += 1
        if imagen[l] != imagen[l-1] or l == len(imagen)-1:
            if n > 4:
                x = '(' + imagen[l-1] + str(n) + ')'
                compr += x
            else:
                compr += imagen[l-1]*n
            n = 1
    return compr


def descomprimirImg(comprimida):
    dcompr = ''
    lista = [j for i in comprimida.split('(') for j in i.split(')') if len(j) > 0]
    for i in lista:
        if i[-1] not in '0123456789':
            dcompr += i   
        else:
            a = 0
            for j in range(len(i)):
                if i[j] not in '0123456789':
                    a = j + 1
            dcompr += i[0] * int(i[a:len(i)]) 
    return dcompr


img = 'NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV'
print(comprimirImg(img))
# (N8)BRAVB((R5)A7)(V5)
print(descomprimirImg(comprimirImg(img)))
# print(img)