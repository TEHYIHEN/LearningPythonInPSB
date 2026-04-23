#greet() is the function
#name is the parameter
def greet(name):

    print(f"Hi there {name}! How are you?")


#main() will always be the first function at call.
#call / invoke / execute -->通常都这么称呼
#- def means define function
#-main is the function name
#- () is the parameter list.In this case it is empty.

def main():

    print("===================")
    print("My First Function")
    print("===================")
    greet("Teh")   # "Teh" is the argument to the function
    greet("lala")
    greet("meme")
    #return main

main()  # call / execute the main() function
greet_friend = input("What is your name? ")
greet(greet_friend)