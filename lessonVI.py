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

def exampleFour():
    print("\nExample Four:")
    file = open('basicFolder/afile.txt', 'w')
    file.write("Hello!")
    file.close

def exampleFive():
    print("\nExample Five:")
    file = open('basicFolder/afile.txt', 'a')
    file.write("Hello agian!")
    file.close

def exampleSix():
    print("\nExample Six:")
    file = open('basicFolder/afile.txt', 'w')
    file.write("Hello!")
    file.close

    file = open('basicFolder/afile.txt', 'a')
    file.write(" Hello agian!")
    file.close

def exampleSeven():
    print("\nExample Seven:")
    content = ["Hello! \n",
               "Hello again! \n"
               "Sh-boom"]
    file = open('basicFolder/afile.txt', 'w')
    file.writelines(content)
    file.close

#==================================================================
# Comment and uncomment as you please to explore specific examples!
#exampleOne()
#exampleTwo()
#exampleThree()
#exampleFour()
#exampleFive()
#exampleSix()
exampleSeven()