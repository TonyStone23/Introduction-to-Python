#Functions---------------------------
import random
def guessingGame(allowedAttempts):
    numberToGuess = random.randint(1, 10)
    guesses = 1
    guessed = False
    while not guessed:
        guess = input(
            f"attempt {guesses}: What number am I thinking of? ")
        if int(guess) == numberToGuess:
            print("You guessed it!")
            guessed = True
        elif guesses == allowedAttempts:
            print("Better luck next time!")
            break # Exit the loop
        else:
            guesses += 1

#Examples---------------------------
def exampleOne():
    print("\nExample One:")
    #----------------
    i = 0
    while i < 10:
        i += 1
    print(i)

def exampleTwo():
    print("\nExample Two:")
    #----------------
    print("I said Don't do this!!")

def exampleThree():
    print("\nExample Three:")
    #----------------
    run = True
    i = 0
    while run:
        i += 1
        if i > 9:
            run = False
    print(i)

def exampleFour():
    print("\nExample Four:")
    #----------------
    print("(see comments)")
    guessingGame(3)

def exampleFive():
    print("\nExample Five:")
    #----------------
    alist = [1, 2, 3]
    blist = []
    for item in alist:
        blist.append(item ** 2)
    print(blist)

def exampleSix():
    print("\nExample Six:")
    #----------------
    alist = [1, 2, 3]
    for i in range(len(alist)):
        alist[i] = alist[i] ** 2
    print(alist)

def exampleSeven():
    print("\nExample Seven:")
    #----------------
    alist = []
    for i in range(1, 4): # Numbers 1-3
        alist.append(i**2)
    print(alist)

def exampleEight():
    print("\nExample Eight:")
    #----------------
    alist = [i**2 for i in range(1, 4)]
    print(alist)

#==================================================================
# Comment and uncomment as you please to explore specific examples!
exampleOne()
exampleTwo()
exampleThree()
exampleFour()
exampleFive()
exampleSix()
exampleSeven()
exampleEight()
