#Examples---------------------------
def exampleOne():
    print("\nExample One:")
    #----------------
    userName = input("What is your name? ")

def exampleTwo():
    print("\nExample Two:")
    #----------------
    num = input("input a number: ")
    print(type(num))

def exampleThree():
    print("\nExample Three:")
    #----------------
    num = input("input a number: ")
    num = int(num) # Typecast string input into an integer
    print(type(num))

def exampleFour():
    print("\nExample Four:")
    #----------------
    userName = input("What is your name? ")
    print("Hello, ", userName) # Add output to greet the user

#==================================================================
# Comment and uncomment as you please to explore specific examples!
exampleOne()
exampleTwo()
exampleThree()
exampleFour()