for row in range(1,9):
    for col in range(1,row+1):
        print("*", end=" ")
    print()



print("="*20)
rows = 8

for i in range(1, rows + 1):

    # 打印空格
    print(" " * (rows - i), end="")

    # 打印星号
    for j in range(1, i + 1):
        print("*", end=" ")

    print()