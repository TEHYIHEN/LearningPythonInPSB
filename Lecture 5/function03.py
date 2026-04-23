import my_function

def main():

    radius = float(input("Enter radius: "))
    circle_area = round(my_function.calculate_circle_area(radius),2)
    circle_perimeter = my_function.calculate_circle_perimeter(radius)
    sphere_volume = my_function.calculate_sphere_volume(radius)
    print("The circle area is: ", circle_area)
    print("The circle perimeter is: ", round(circle_perimeter,2))
    print(f"The sphere volume is: {round(sphere_volume,2)}")  #{sphere_volume:.2f}
    print("The hemisphere area is: ", my_function.calculate_hemisphere_surface_area(radius))
    print("The surface area is: ", my_function.calculate_sphere_surface_area(radius))

main()