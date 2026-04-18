#Summation series:
#2,7,12,17,22,32,37....52

#sum up in steps of 5 form 2 to not exceeding 1000
#find the average
total = 0
count = 0
for i in range(2,53,5):  #start=2, end=53, step=5
    total += i
    count += 1

print(f"Count: {count}")
print(f"Total:{total}")
print(f"Average:{total/count}")