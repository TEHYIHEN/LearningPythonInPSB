def find_median(number_list):
    """Assume that number_list is not empty"""
    sorted_numbers = sorted(number_list)    #first sort
    #[1,3,6,7,8,9,10]  then median =7

    if len(number_list) % 2 == 1:    #odd number, get middle value
        middle_index = len(number_list) // 2    #int(3.5) =3
        median = sorted_numbers[middle_index]
    else:
    # [1,3,5,7,8,9,10,11]  then median = (7+8）/2
        middle_right = len(number_list) // 2   #8
        middle_left = middle_right - 1    #7
        median = sorted_numbers[middle_left] + sorted_numbers[middle_right]
        median = median / 2

    return median

def add_zero(a):   #pass by reference
    a.append(0)

def add_number(number):
    number = 9999   # need to put return

def main():
    number_list_1 = [1,3,5,7,8,9,10]
    print(find_median(number_list_1))
    number_list_2 = [1,3,5,6,7,8,9,10]
    print(find_median(number_list_2))

    print()
    print("=== test add_zero ===")
    add_zero(number_list_1)
    print(number_list_1)

    print()
    print("=== test add_number  ===")
    number = 10
    print(add_number(number))


main()

