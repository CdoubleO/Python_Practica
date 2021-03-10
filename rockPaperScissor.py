from random import choice

def isWin(player_choice, computer_choice) :
    choices = ("r","p","s")
    #player_choice = choices.index(player_choice)
    #computer_choice = choices.index(computer_choice)
    if player_choice - computer_choice == -1 :
        return False
    return True


def play() :
    while True :
        player_choice = input("(R) for rock, (P) for paper, (S) for scissors or (Q) to quit!\n >> ").lower()
        computer_choice = choice(("r","p","s"))
        if player_choice == "q" :
            break
        print(f"{player_choice} vs {computer_choice}")
        if player_choice == computer_choice :
            print("It's a tie!")
        elif isWin(player_choice, computer_choice) :
            print("You win!")
        else :
            print("You lose!")
    

play()