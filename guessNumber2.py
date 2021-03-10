import random

def guess(upper_bound) :
    number = random.randint(1,upper_bound)
    max_tries = 3
    tries = 0
    while tries < max_tries :
        guess_input = int(input(f"Guess the number between 1 and {upper_bound}: "))
        tries += 1
        if guess_input == number :
            print(f"Correct! The number was: {guess_input}. It only took you: {tries}")
            tries = 0
            break
        elif tries == max_tries:
            print(f"Incorrect! Sorry no more tries!\nThe number was {number}")
        elif guess_input < number :
            print(f"Incorrect! Guess higher next time!! You have {max_tries - tries} tries left.")  
        else :
            print(f"Incorrect! Guess lower next time!! You have {max_tries - tries} tries left.")  
      

def computerGuess(n) :
    upper_bound = n
    lower_bound = 1
    max_tries = 3
    tries = 0
    feedback = ""
    while feedback != "c" and tries < max_tries:
        if lower_bound == upper_bound :
            computer_guess = upper_bound
        else :
            computer_guess = random.randint(lower_bound,upper_bound) 
        tries += 1
        feedback = input(f"is {computer_guess} the correct number?\n * Enter (h) if it is too high\n * Enter (l) if it is too low\n * Enter (c) if it is correct\n >>  ").lower()
        while feedback not in ("c","l","h") :
            feedback = input("sorry i dont understand! please try again\n >>  ")
        if feedback == "l" :
            lower_bound = computer_guess + 1 
        elif feedback == "h" :
            upper_bound = computer_guess - 1
        else:
            print(f"Computer wins! it took {tries} tries")


def play() :
    command = ""
    while(command != "n") :
        command = input("Play? (y/N): ").lower()
        if command == "y" :
            limit = int(input("Set limit: "))
            guess(limit)
            print("ok! now it is my turn!")
            limit = int(input("Set limit: "))
            computerGuess(limit)
        elif command != "n" :
            print("bye...")
        else :
            print("Sorry i dont understand!")


play()

