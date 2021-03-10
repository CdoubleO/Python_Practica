'''
1)pedir al usuario un mensage (formato string)
    a)pedir un input
2)encriptar mensaje
    a)tomar el string del input
    b)se tiene un string de letras y otro string de las mismas letras pero mescaladas
    c)tomar la primer letra del mensaje y la busca en el string de letras ysaca el indice
    d)con ese indice va a buscar en el otro string que letra estya en esa posicion
    e)se repite hasta traducir todo el mensaje
3)devolver al usuario el mensaje encriptado
4)pedir al usuario un mensaje encriptado
5)desencriptar mensaje
6)devolver el mensaje descencriptado
'''
from random import shuffle

msj = input("Ingrese mensaje a encriptar: ")

SYMBOL_SET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

msj_encr = ""

#genre llave de encriptacion
"""
key = list(SYMBOL_SET)
shuffle(key)
key = "".join(key)
"""
key = "FSZLPJRÑGIAWKBDVXONQMTYUEHC"
print(f"LLave: {key}")

#encriptado
for i in msj:
    if i.upper() in SYMBOL_SET:
        idx = SYMBOL_SET.find(i.upper())
        char = key[idx]
        if i.islower():
            char = char.lower()
        msj_encr += char
    else:
        msj_encr += i
print(f"mensaje: {msj}\nencriptado: {msj_encr}")


#desencriptado
msj_desc = ""
for i in msj_encr:
    if i.upper() in key:
        idx = key.find(i.upper())
        if i.isupper():
            msj_desc += SYMBOL_SET[idx]
        else:
            msj_desc += SYMBOL_SET[idx].lower()
    else:
        msj_desc += i

print(f"mensaje: {msj_encr}\ndesencriptado: {msj_desc}")


















