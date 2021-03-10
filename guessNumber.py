import random

def guess(n):
    number = random.randint(1,n)
    max_tries = 3
    tries = 0
    while (True):
        if tries == max_tries:
            print(f"sorry! no more tries!\nthe number was {number}")
            break
        guess_input = int(input("guess the number: "))
        if guess_input == number:
            print("Correct!")
            break
        else:
            print("incorrect! guess again!")
        tries += 1

def play():
    while(True):
        command = input("play? (y/n): ")
        if command.lower() == "y":
            guess(10)
        else:
            break

play()