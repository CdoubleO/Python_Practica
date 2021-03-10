from sys import exit
from random import shuffle

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getRandomKey()-> str:
    key = list(LETTERS)
    shuffle(key)
    return "".join(key)


def checkValidKey(key: str)-> None:
    key_list = list(key)
    key_list.sort()
    if key_list != list(LETTERS):
        exit("Error in key!")
    

def getFinalMessage(key: str,message: str,mode: str)-> str:
    final_msg = ""
    str_A, str_B = LETTERS, key
    if mode.lower().startswith('d'):
        str_A, str_B = str_B, str_A
    for char in message:
        if char.upper() in str_A:
            idx_char = str_A.find(char.upper())
            if char.isupper():
                final_msg += str_B[idx_char].upper()
            else:
                final_msg += str_B[idx_char].lower()
        else:
            final_msg += char
    return final_msg

    
def main()-> None:
    
    msg = input("Enter message:\n>>> ")
    key = input("Generate Key? (y/n):\n>>> ")
    mode = input("Encrypt (e) / Decrypt (d):\n>>> ")
    if mode.lower().startswith('e') and key.lower().startswith('y'):
        key = getRandomKey()
    else:
        key = input("Enter key:\n>>> ")

    checkValidKey(key)

    
    print(f"Key: {key} Message: {getFinalMessage(key,msg,mode.lower()[0])}")


    

if __name__ == "__main__":
    main()
