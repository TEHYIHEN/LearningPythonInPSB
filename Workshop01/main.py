from Teh_Yi_Hen_solution import *

def main():
    print("=" * 50)
    print("♂️Student Details👨")
    print()
    myName, myEmail, myBBUsername = studentname()
    print(f"{'Name':10}"+ ":" , myName)
    print(f"{'Email':10}"+ ":", myEmail)
    print(f"{'StudentID':10}"+ ":", myBBUsername)
    print()
    print("=" * 50)

    print("✏️ Answer of Question 1")
    print()
    arraylist = [2,6,8,3,4,6]
    print(calAverage(arraylist))
    print()
    print("=" * 50)

    print("✏️ Answer of Question 2")
    print()
    character = "Hell0 WorlD!!!4567"
    print(countCharacter(character))
    print()
    print("=" * 50)

    print("✏️ Answer of Question 3")
    print()
    list_1 = [1,2,3,4,2,1]
    list_2  = [2,4,4,2]
    print(excludeItem(list_1, list_2))
    print()
    print("=" * 50)

    print("✏️ Answer of Question 4")
    print()
    arraylist1 = [1,2,3,4,5,6]
    arraylist2 = [6,8,3,4,6]
    arraylist3 = [53,23]
    arraylist4 = [13]
    arraylist5 = [12, "not number", 23]
    print(secondLarge(arraylist1))
    print(secondLarge(arraylist2))
    print(secondLarge(arraylist3))
    print(secondLarge(arraylist4))
    print(secondLarge(arraylist5))
    print()
    print("=" * 50)

    print("✏️ Answer of Question 5")
    print()
    print(isValidPassword("abc"))  #
    print(isValidPassword("abcdefghij"))  # False
    print(isValidPassword("ABC1234567"))  # False
    print(isValidPassword("Abc1234567"))  # False
    print(isValidPassword("Abc12345!"))  # False
    print(isValidPassword("Abc12345! "))  # True (with whiteSpace)

main()