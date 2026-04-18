# Write a program that asks the user to enter the number of times that
# he/she have run around a racetrack, and then use a loop to prompt him/her
# to enter the lap time for each of his/her lap
# When the loop finishes, the program should display the time of the fastest lap,
# the time of the slowest lap, and the average lap time

num_rounds = int(input("Enter number of rounds: "))

total = 0
fastest = None
slowest = None

for i in range(num_rounds):
    time_taken = float(input(f"Timing in round {i+1} in seconds? "))
    total += time_taken

    if fastest is None or time_taken < fastest:
        fastest = time_taken

    if slowest is None or time_taken > slowest:
        slowest = time_taken

print()
if num_rounds > 0:
    print("==============Your stars==========")
    print(f"Total time taken: {total:.2f} seconds")
    print(f"Average time taken: {total / num_rounds:.2f} seconds")
    print(f"Slowest time taken: {slowest:.2f} seconds")
    print(f"Fastest time taken: {fastest:.2f} seconds")


