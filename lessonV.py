# Functions
def findCharacterBasic(astring, achar):
    for c in astring:
        print("found") if achar is c else print("not found")

def findCharacterEdited(astring, achar):
    found = False
    for c in astring:
        if achar is c:
            found = True
    return found

def parseCharacter(astring, achar):
    found = False
    notChar = []
    for c in astring:
        if achar is c:
           found = True
        else:
            notChar.append(c)
    return found, notChar

#Examples---------------------------
def exampleOne():
    print("\nExample One:")
    #----------------
    char = 'a'
    for c in "Hello":
        print("found") if char is c else print("not found")

def exampleTwo():
    print("\nExample Two:")
    #----------------
    findCharacterBasic("sue", "s")

def exampleThree():
    print("\nExample Three:")
    #----------------
    check = findCharacterEdited("sue", "s")
    if check is True:
        print("found")
    else:
        print("not found")

def exampleFour():
    print("\nExample Four:")
    #----------------
    checkIncluded, nots = parseCharacter("sue", "s")
    print(checkIncluded, nots)

#==================================================================
# Comment and uncomment as you please to explore specific examples!
exampleOne()
exampleTwo()
exampleThree()
exampleFour()
