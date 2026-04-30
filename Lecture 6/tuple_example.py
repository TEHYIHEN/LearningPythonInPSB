numbers = [1, 2, 3, 4, 5]  # a list.
numbers.append(10)         # can append
numbers[0] = 99            # can modify
print(numbers)

#Tuple is a READ-ONLY list
MONTH_NAMES = (
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
)
print(MONTH_NAMES)

# 下面这两行在运行时会报错，因为元组不可修改：
#MONTH_NAMES[0] = "Jan"
#MONTH_NAMES.append("13th month")