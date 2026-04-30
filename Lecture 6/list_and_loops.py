age_list = [6,7,5,4,13,12,9,10,8]

#for each loop
for age in age_list: #age is read-only
    age = age + 1
    print(age)
print("=== after the for each loop ===")
print("age_list:",age_list)  # it wont replace result in the original list
print("--" * 10)

print()
# indexed for loop
for i in range(len(age_list)):
    age_list[i] = age_list[i] + 1
    print(age_list[i])
print("=== after the indexed loop ===")
print("age_list：", age_list) #📌it replace result in the original list
print("--" * 10)