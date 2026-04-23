superstar = "BTS"   ##Global Variable

def find_local_star():

    local_star = "Steven Lim"  ##Local variable
    print(f"Inside find_local_star(): {local_star}")

def main():

    print(f"Global:{superstar}")
    find_local_star()
    print(f"{local_star}")  ##error : because this is variable(local) inside the function find_local_star
    print("End of program")

main()

#Global variable are accessible everywhere
#Local variables are accessible only within the function
#Rule of thumb:
#1. Use as little global variables as possible, if possible NONE
#2. Use local variables most of the time or all of the time