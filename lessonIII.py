#Examples---------------------------
def exampleOne():
    print("\nExample One:")
    #----------------
    print("\nAND")
    # 'AND' operator is 'and'
    print(True and False)
    print(True and True) 
    print(False and False) 

    print("\nOR ")
    # 'OR' operator is 'or'
    print(True and False) # Output: True
    print(True and True) # Output: True
    print(False and False) # Output: False

    print("\nNOT")
    # 'NOT' operator is 'not'
    print(not False) # Output: True
    print(not True) # Output: False

def exampleTwo():
    print("\nExample Two:")
    #----------------
    print("\nInequalities")
    # value comparison using <, >, <=, =>
    anum = 5
    bnum = 6
    print(anum > bnum) # Output: False
    print(anum < bnum) # Output: True

    print("\nTypecasting")
    # typecasting bool
    print(bool(1)) # Output: True (Values larger than 1 are true)
    astr = ""
    bstr = "any string"
    alist = []
    blist = ["at least one item"]
    print(bool(astr)) # Output: False
    print(bool(bstr)) # Output: True
    print(bool(alist)) # Output: False
    print(bool(blist)) # Output: True

    print("\nNOT")
    # In case you need the opposite:
    print(not astr) # Output: True
    print(not bstr) # Output: False
    print(not alist) # Output: True
    print(not blist) # Output: False
    # Note, you don't need to explicitly 
    # typecaste with 'bool' when using not

def exampleThree():
    print("\nExample Three:")
    #----------------
    age = int(input("How old are you"))
    if age < 13:
        print(":D")

def exampleFour():
    print("\nExample Four:")
    #----------------
    age = int(input("How old are you"))
    if age < 13:
        print(":D")
    else:
        print("hello")

def exampleFive():
    print("\nExample Five:")
    #----------------
    age = int(input("How old are you"))
    if age < 7:
        print(":D")
    elif age < 13:
        print(":)")
    else:
        print("hello")

#==================================================================
# Comment and uncomment as you please to explore specific examples!
exampleOne()
exampleTwo()
exampleThree()
exampleFour()
exampleFive()