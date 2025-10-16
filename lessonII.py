#Examples---------------------------
def exampleOne():
    print("\nExample One:")
    #----------------
    alist = ["my", "name", "is", "Tony"]
    print(alist[0])
    print(alist[2])
    print(alist[3])
    print(alist[-1])

def exampleTwo():
    print("\nExample Two:")
    #----------------
    nums = [1, 2, 3, 4, 5]
    sumTwo = nums[3] + nums[4] # 4 + 5
    print(sumTwo)

def exampleThree():
    print("\nExample Three:")
    #----------------
    alist = ["my", "name", "is", "Tony"]
    print(alist[1:4])

def exampleFour():
    print("\nExample Four:")
    #----------------
    nums = [1, 2, 3, 4, 5]
    nums = nums + [6]
    print(nums) 
    nums = nums + nums
    print(nums)
    newNums = nums[0:2]+nums[10:12]
    print(newNums)

def exampleFive():
    print("\nExample Five:")
    #----------------
    alist = [i for i in range(5)]
    print(alist)

#==================================================================
# Comment and uncomment as you please to explore specific examples!
exampleOne()
exampleOne()
exampleTwo()
exampleThree()
exampleFour()
exampleFive()