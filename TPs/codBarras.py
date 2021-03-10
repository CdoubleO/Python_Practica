'''
TP8
'''
def solucion(entrada):
    tabla = {
    '0' : 'EEUU',
    '539' : 'Irlanda',
    '759' : 'Venezuela',
    '380' : 'Bulgaria',
    '560' : 'Portugal',
    '850' : 'Cuba',
    '50' : 'Inglaterra',
    '70' : 'Noruega',
    '890' : 'India'}
    l = len(entrada)
    if  l < 8:
        entrada = '0' * (8 - l) + entrada
        l = 8
    elif 8 < l < 13:
        entrada = '0' * (13 - l) + entrada
        l = 13
    entrada = entrada[::-1]
    check = 0
    for i in range(1,l):
        x = int(entrada[i])
        if i % 2 == 1:
            x *= 3
        check +=  x
    check +=  int(entrada[0])   
    if check % 10 == 0:
        check = 'SI'
    else:
        check = 'NO'
    if l == 13 and check == 'SI':
        for k in tabla:
            if k == entrada[l-1:l-1-len(k):-1]:
                pais = tabla[k]
                return f'{check} {pais}'
            return f'{check} Desconocido'
    return check



cod = '5029365779425'
print(solucion(cod))
