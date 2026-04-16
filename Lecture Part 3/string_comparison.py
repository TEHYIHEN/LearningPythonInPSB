string_1 = "bat"
string_2 = "bag"

# ASCII Table
# "t" is greater than "g"

print(string_1 == string_2)   #False
print(string_1 != string_2)   #True
print(string_1 > string_2)    #True
print(string_1 < string_2)    #False

print("======Other Case=======")
string_3 = "Bat"

# "B" is smaller than "b" in ASCII Table
print(string_3 == string_1)  #False
print(string_3 != string_1)  #True
print(string_3 > string_1)   #False
print(string_3 < string_1)   #True