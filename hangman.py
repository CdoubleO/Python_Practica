def getRandomWord() :
    # hardcoded - fix later
    return "test"


def isLetterInWord(letter, word) :
    if letter in word :
        return True
    return False 


def isWin(display_word, word) :
    if display_word == word :
        return True
    return False


def showDisplay(display_word, lifes, guesses) :
    return f"Word: {display_word}\nLifes: {lifes}\nPrevious guesses: {guesses}"


def play() :
    word = getRandomWord()
    display_word = "*" * len(word)
    lifes = 7
    guesses = []
    while not isWin(display_word, word) :
        print(showDisplay(display_word, lifes, guesses))
        guess = input("Guess a letter!\n >> ")
        guesses.append(guess)
        if isLetterInWord(guess,word) :
            letter_position = word.index(guess)
            display_word = f"{display_word[:letter_position]}{guess}{display_word[letter_position + 1:]}"
            if isWin(display_word, word) : 
                print(f"you win!\nThe word was: {word}")
                break
        else :
            lifes -= 1
            if lifes < 1 :
                print(f"Sorry you lost! The word was {word}")


feedback = input("Play? y/n\n >> ")
while feedback != "n" :
    play()