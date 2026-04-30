fruits = ["apple", "pineapple", "durian", "banana",
          "cherry", "pear", "honeydew", "rock melon",
          "watermelon", "starfruit", "mangosteen"]

# slice = list[start:end:step], where end is excluded
fruits_1 = fruits[:4]  #index 0, 1, 2, 3
print(fruits_1)

print()
fruits_2 = fruits[2:7]  #index 2,3,4,5,6
print(fruits_2)

print()
fruits_3 = fruits[7:] #index 7 to end
print(fruits_3)

print()
#start 1 , end 8 , action +2
fruits_4 = fruits[1:8:2]  #index 1,3,5,7
print(fruits_4)

print()
fruits_5 = fruits[::-1] #reverse
print(fruits_5)