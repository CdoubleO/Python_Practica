from random import shuffle
from sys import exit

SYMBOL_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def obtenerLLaveEncriptado(simbol_set):
    key = list(simbol_set)
    shuffle(key)
    key = "".join(key)

    if verificarLLave(key, simbol_set):
        return key
    return exit("Error al generar la llave")


def verificarLLave(key, simbol_set):
    var = list(key)
    var.sort()
    var = "".join(var)
    if var == simbol_set:
        return True
    return False


def encriptarMensaje(msj, simbol_set, key):
    msj_encr = ""
    for i in msj:
        if i.upper() in simbol_set:
            idx = simbol_set.find(i.upper())
            char = key[idx]
            if i.islower():
                char = char.lower()
            msj_encr += char
        else:
            msj_encr += i
    return msj_encr


def desencriptarMensaje(msj_encr, simbol_set, key):
    msj_desc = ""
    for i in msj_encr:
        if i.upper() in key:
            idx = key.find(i.upper())
            if i.isupper():
                msj_desc += simbol_set[idx]
            else:
                msj_desc += simbol_set[idx].lower()
        else:
            msj_desc += i
    return msj_desc


def main():
    while True:
        ask = input("Encriptar (e)/ Desencriptar (d)/ salir (s): ")

        if ask.lower().startswith('s'):
            break
        elif ask.lower().startswith('e'):
            ask = input("Generar llave? y/n: ")
            if ask.lower().startswith('y'):
                key = obtenerLLaveEncriptado(SYMBOL_SET)
            elif ask.lower().startswith('n'):
                key = input("Ingresar Llave: ")
                if not verificarLLave(key, SYMBOL_SET):
                    exit("not a valid key!")
            else:
                exit("input error")

            msj = input("mensaje: ")
            encriptado = encriptarMensaje(msj, SYMBOL_SET, key)
            print(f"Mensaje: {msj}\nLlave: {key}\nOutput: {encriptado}")
            

        elif ask.lower().startswith('d'):
            msj = input("mensaje: ")
            key = input("Ingresar Llave: ")
            if not verificarLLave(key, SYMBOL_SET):
                exit("not a valid key!")
            desencriptado = desencriptarMensaje(msj, SYMBOL_SET, key)
            print(f"Mensaje: {msj}\nLlave: {key}\nOutput: {desencriptado}")
        else:
            print("opcion no valida!")
            continue
    





if __name__ == "__main__":
    main()

















