from coin import Coin

def main():

    """Start of program."""
    coins = []
    for i in range(3):
        coins.append(Coin())

    for i in range(len(coins)):
        coins[i].toss()
        print(coins[i].get_side_up())

    print()
    print("===============================")
    print()
    coins[0].side_up = "Heads"
    coins[1].side_up = "Heads"
    coins[2].side_up = "Heads"
    for i in range(len(coins)):
        print(coins[i].get_side_up())


if __name__ == "__main__":
    main()
