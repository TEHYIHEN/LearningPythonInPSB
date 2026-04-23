def add_there(a, b, c):
    total = a + b + c
    print(total)

def change_this(x):
    print(f"Value of argument: {x}")
    print("Changing to +100")
    x = x + 100
    #print(x)

def announce_winners(champion, first_runner_up, second_runner_up):
    print(f"The 2nd runner up is: {second_runner_up}")
    print(f"The champion is: {champion}")
    print(f"1st runner up is: {first_runner_up}")

def main():
    add_there(4, 5, 6)  #15
    number = 99
    change_this(number)     ##pass by value , result = 99
    print("Number after changing: ", number)

    runner_1 = "Lucky"
    runner_2 = "Brave"
    champ = "Champ"
    announce_winners(runner_1, runner_2, champ)

main()
#change_this(99)