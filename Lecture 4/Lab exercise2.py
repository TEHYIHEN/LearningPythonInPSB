#The area of a rectangle is the rectangle's length times its width.
#Write a program that asks for the length and width of two rectangles.
#The program should tell the user which rectangle has the greater area,
#iof if the areas area the same.

length_1 = int(input("Enter length of first sequence: "))
width_1 = int(input("Enter width of first sequence: "))

length_2 = int(input("Enter length of second sequence: "))
width_2 = int(input("Enter width of second sequence: "))

area_1 = length_1 * width_1
area_2 = length_2 * width_2

if area_1 > area_2:
    print("Area of rectangle 1 is greater than area of rectangle 2")
elif area_1 < area_2:
    print("Area of rectangle 1 is less than area of rectangle 2")
else:
    print("Areas of both rectangles are equal")