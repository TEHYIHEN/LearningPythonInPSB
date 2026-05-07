message = "trusted education provider"


print(message[:7]) # start =0, end=7 , step=1
#trusted
print(message[8:17]) #start = 8, end = 17, step = 1
#education
print(message[1:17:2]) #start = 1, end = 17, step = 2
#rse dcto


print()
print("="*20)
print()

if "tion" in message:
    print("Found in message") #educa(tion) , so founded
else:
    print("Not Found in message")


if "private" not in message:
    print("private not found") # not found
else:
    print("private found")
