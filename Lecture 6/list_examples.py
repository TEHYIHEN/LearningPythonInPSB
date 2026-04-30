numbers = [5, 7, 19, 20, 31, 4, 2]
#index     0  1   2   3   4  5  6
#         -7 -6  -5  -4  -3 -2 -1

print(numbers)
print(type(numbers))
print(numbers[0]) # first item, 5
print(numbers[-7]) # first item
print(numbers[6]) # last item, 2
print(numbers[-1]) #last item

print(numbers[len(numbers)-1])  # index 6 , because 7 -1

print()
print("==" * 10)
print()
numbers[0] = 99   #modify first item
print(numbers)  #[99, 7, 19, 20, 31, 4, 2]

print()
print("==" * 10)
print()
namelist = [{"Teh", 7}, {"Tom", 5}]
print(namelist)
print(namelist[0])
