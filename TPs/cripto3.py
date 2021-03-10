'''
TP5
Método de encriptación creado por León Battista Alberti (1402-1472), considerado como
el abuelo de la criptografía. El método consiste en hacer un doble cifrado usando dos
alfabetos. Realizar una función que permita cifrar un mensaje por este método
'''
def encriptar(msj):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha1 = 'FRJOYDIQTZSLMEUNBKWAHPCXGV'
    alpha2 = 'HTRVZDIQJYPELMUBNKAWFSXCGO'
    letras = ''
    for l in msj:
        if l in alpha:
            letras += l
    encr = ''
    print(letras)
    for i in range(len(letras)):
        x = alpha.index(letras[i])
        print(x)
        if i % 2 == 0:
            encr = encr + alpha1[x]
        else:
            encr = encr + alpha2[x]
        print(encr)
    return encr


msj = input('Ingrese mensaje a encriptar: ')
print('Mensaje encriptado: ', encriptar(msj))