#Examples---------------------------
def exampleOne():
    print("\nExample One:")
    #----------------
    file = open('basicFolder/basicFile.txt')
    print(file)
    file.close()

def exampleTwo():
    print("\nExample Two:")
    #----------------
    file = open('basicFolder/substantFile.txt')
    fileContent = file.read()
    print(fileContent)
    file.close()

def exampleThree():
    print("\nExample Three:")
    #----------------
    file = open('basicFolder/substantFile.txt')
    fileContent = file.read()
    print(fileContent.split('\n')[-1])
    file.close()

#==================================================================
# Comment and uncomment as you please to explore specific examples!
exampleOne()
exampleTwo()
exampleThree()