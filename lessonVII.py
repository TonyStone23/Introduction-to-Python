#Examples---------------------------
def exampleOne():
    print("\nExample One:")
    #----------------
    print(3/0)

def exampleTwo():
    print("\nExample Two:")
    #----------------
    try:
        print(3/0)
    finally:
        print("Program executed")

def exampleThree():
    print("\nExample Three:")
    #----------------
    try:
        print(3/0)
    except Exception as e:
        print(e,"happened")
    finally:
        print("Program executed")

def addNum(a, b):
    if type(a) is str or type(b) is str:
        raise ValueError("That is not a number!")
    return a + b

def exampleFour():
    print("\nExample Four:")  
    #----------------
    sum = None  
    try:
        sum = addNum(1, "astring")
    except Exception:
        print("Ugh-oh")
    finally:
        print(sum)
   

def exampleFive():
    print("\nExample Five:")
    #----------------
    file = open('basicFolder/nonExistantFile.txt', 'r')
    contents = file.read()
    print(contents)
    file.close()

def exampleSix():
    print("\nExample Six:")
    #----------------
    fileName = 'basicFolder/nonExistantFile.txt'
    contents = None
    try:
        file = open(fileName, 'r')
        contents = file.read()
        file.close()
    except FileNotFoundError:
        print(fileName, "doesn't exist")
    finally:
        print(contents)
    
def exampleSeven():
    print("\nExample Seven:")
    #----------------
    fileName = 'basicFolder/substantFile.txt'
    contents = None
    try:
        file = open(fileName, 'r')
        contents = file.read()
        file.close()
    except FileNotFoundError:
        print(fileName, "doesn't exist")
    finally:
        print(contents)

#==================================================================
# Comment and uncomment as you please to explore specific examples!
#exampleOne()
#exampleTwo()
#exampleThree()
#exampleFour()
#exampleFive()
#exampleSix()
exampleSeven()