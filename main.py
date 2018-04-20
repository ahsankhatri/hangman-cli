import random
import time

def askForLetter():
    userInput = raw_input("\n>>> Guess your letter: ").upper()

    if not userInput:
        return askForLetter()

    return userInput[0]

def printGuessWord(letter):
    global guessWord, word

    for i,x in enumerate(word):
        if x==letter:
            guessWord[i] = letter

    return " ".join(guessWord)

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def startTime():
    global startedTime

    if startedTime == 0:
        startedTime = time.time()

if __name__=="__main__":
    word           = list(random_line('dictionary.txt').upper())
    guessWord      = ['_'] * len(word)
    attempts       = startedTime = 0
    alreadyGuessed = []

    print ">>> Welcome to Hangman! Try to guess the word with minimum attempts."
    print " ", "_ " * len(word)

    while word != guessWord:
        letter = askForLetter()

        startTime() # Start timer

        # Already guess intimation
        try:
            if letter in alreadyGuessed:
                print "You have already guessed this letter, please guess another one.\n"
                continue
        except Exception:
            pass

        attempts += 1
        alreadyGuessed.append(letter)

        # Incorrect intimation
        try:
            if letter not in word:
                print "Incorrect!"
                continue
        except Exception:
            pass

        print " ", printGuessWord(letter)

    diff = int(time.time() - startedTime)
    minutes, seconds = diff // 60, diff % 60
    print "\n", "Congratulations! You guess the correct word in", attempts, "attempts and you took " + str(minutes).zfill(2) + ':' + str(seconds).zfill(2), 'seconds'

    # Save user data for future statistics
    with open('history.txt', 'a') as historyFile:
        historyFile.write("".join(word)+'|'+str(attempts)+'|'+str(diff)+"\n")
