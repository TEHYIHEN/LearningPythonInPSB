def studentname():
    myName = "Teh Yi Hen"
    myEmail = "tehyihen1994@gmail.com"
    myBBUsername = "707PKCSC"

    return myName, myEmail, myBBUsername

'''QUESTION 1'''
'''Define a function named "calAverage" which take a list of integers as parameter. 
This function will then calculate and store the average into a variable named "result". 
Finally, the function MUST return the result with 2 decimal place only. 
For Example given the following list,
[2,6,8,3,4,6], the function will return 4.83 (float). '''

def calAverage(a):

    total = sum(a)
    count = len(a)
    result = round((total / count),2)

    return result

'''QUESTION 2'''
'''Define a function named "countCharacter" that accepts a sentence as parameter (string) 
and calculate 
the total number of letters, 
total number of uppercase letters, 
total number of lowercase letters, 
total number of digits 
and total number of characters that is not letter and not digit.
The function will then return a list of integer representing total number of letters , 
number of letters with uppercase and lowercase, 
number of digits and any other character beside letters and digits.
Suppose the following input is supplied to the function
"Hell0 WorlD!!!4567" the function will return a list with the following values
[9, 3, 6, 5, 4]'''

def countCharacter(sentence):

    total_num_letters = 0
    total_num_uppercase = 0
    total_num_lowercase = 0
    total_num_digits = 0
    others_characters = 0

    for char in sentence:
        if "A" <= char <= "Z":
            total_num_letters += 1
            total_num_uppercase += 1
        elif "a" <= char <= "z":
            total_num_letters += 1
            total_num_lowercase += 1
        elif "0" <= char <= "9":
            total_num_digits += 1
        else:
            others_characters += 1

    final_result = [
                    total_num_letters,
                    total_num_uppercase,
                    total_num_lowercase,
                    total_num_digits,
                    others_characters
                    ]
    return final_result

'''Question 3'''
'''Define a function named "excludeItem" which take two parameters (item1 & item2) and both
are list. This function will create a separate list named "result" which only include items 
found in both lists. The result list should not have duplicate value.
For example, given item1 = [1,2,3,4,2,1] while item2 = [2, 4, 4, 2]. 
This function will return a result of [2,4]. 
Note that the output value is unique (no duplicate). The function must be able
to accept other parameters as well i.e. list of strings or mixture of strings and digits'''

def excludeItem(item1, item2):

    result = []

    for item in item1:

        if item not in item2:
           continue

        if item in result:
            continue

        result.append(item)

    return result

'''QUESTION 4'''
'''Define a function named "secondLarge" which take a list of numbers (integer) as parameter.
This function will then identify and return the 2nd largest number in the list. 
The function will return smallest number if the parameter only contains two numbers. 
While the function will return the only number if the list contain only single number.
On some odd case, the function will return -999 
if the parameter contains other datatype i.e. string or float in the list.
'''
'''FOR EXAMPLE:
• [1,2,3,4,5,6] returns 5
• [6,8,3,4,6] returns 6
• [53, 23] return 23
• [13] return 13
• [12, 'not number', 23] return -999
'''

def secondLarge(numbers):

    checking_list = []

    for number in numbers:

        if not isinstance(number, int):
            return -999

        if number in checking_list:
            continue

        checking_list.append(number)
        checking_list.sort()

    second_large = checking_list[len(checking_list) - 2]

    return second_large

'''QUESTION 5'''
'''Define a function named "isValidPassword" which take a string as parameter. 
The function will then check if the supplied string fulfilled the following password criterias:
1) must have combination of uppercase and lowercase
2) must have at least 3 digits
3) must have at least 2 special character (including whitespace).
4) must have at least 10 characters (combination of alphanumeric and special symbol)
The function will return a Boolean value i.e. True if all criterias are met or return False
otherwise.
Make sure you test your function with every single possible input that may return False value
as well.
'''

def isValidPassword(password):

    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_char_count = 0

    for char in password:

        if "a" <= char <= "z":
            lowercase_count += 1
        elif "A" <= char <= "Z":
            uppercase_count += 1
        elif "0" <= char <= "9":
            digit_count += 1
        else:
            special_char_count += 1


    if len(password) < 10:
        #return "Password must be at least 10 characters"
        return False
    elif uppercase_count == 0 or lowercase_count == 0:
        #return "Password must combination of uppercase and lowercase"
        return False
    elif digit_count < 3:
        #return "Password must have at least 3 digits"
        return False
    elif special_char_count < 2:
        #return "Password must have at least 2 special characters"
        return False

    return True




