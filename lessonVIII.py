#Functions--------------------------
def bounds(value, boundarySize):
    lowerBound = value - boundarySize
    upperBound = value + boundarySize
    return lowerBound, upperBound

#Examples---------------------------
def exampleOne():
    print("\nExample One:")
    #----------------
    atuple = (1, 2, 3)
    print(atuple[1])


#Examples---------------------------
def exampleTwo():
    print("\nExample Two:")

    lb, ub = bounds(10, 2)
    print(lb, ub)
    #----------------

#Examples---------------------------
def exampleThree():
    print("\nExample Three:")

    result = bounds(10, 2)
    print(type(result), result)
    #----------------

#Examples---------------------------
def exampleFour():
    print("\nExample Four:")

    aset = {1, 2, 3}
    aset.add(4)
    print(aset)
    aset.add(5)
    print(aset)
    aset = aset | {6, 7} # Union
    print(aset)
    aset = aset | {2, 3} # Union
    print(aset)
    aset.remove(4)
    print(aset)
    aset = aset - {1, 2, 3} # Differnce
    print(aset)
    aset = aset & {7, 8, 9} # Intersection
    print(aset)
    aset.remove(7)
    print(aset)
    #----------------

#Examples---------------------------
def exampleFive():
    print("\nExample Five:")

    aset = {1, 2, 3}
    bset = {3, 4, 5}

    cset = aset | bset
    if 4 not in cset:
        cset.add(4)
    else:
        cset.add(0)
    print(cset)
    #----------------

    
#==================================================================
# Comment and uncomment as you please to explore specific examples!
exampleOne()
exampleTwo()
exampleThree()
exampleFour()
exampleFive()