#for item in ... :                   # for each loop
#statement(s)
#Usage: Fixed number of iterations

for char in "Mountain":
    print(char)

print("-" * 50)
for item in ["Pen", "Pencil" , "Eraser"]:
    print(item)

#for i in range(start, end, step):
#statement(s)                        #index for loop

print("-" * 50)
for i in range(5):      # start = 0, end = 5 , step =1
    print(i)            # exclude end   #result will be [0,1,2,4]

print("-" * 50)
for i in range(3,8):    # start = 3, end = 8 , step =1
    print(i)            #3,4,5,6,7

print("-" * 50)
for i in range(1,11,2): # start=1 , end =11 , step = 2
    print(i)            #1,3,5,7,9