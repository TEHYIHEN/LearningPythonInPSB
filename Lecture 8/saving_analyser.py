def read_data(filename):
    saving_list = []  # a list of floats read from the file.
    file_in = open(filename, "r")

    for line in file_in:
        line = line.strip()

        if line == "":
            continue

        amount = float(line)
        saving_list.append(amount)

    file_in.close()
    return saving_list


def main():

    saving = []

    #1. read the saving.txt into a list of savings

    saving = read_data("saving.txt")
    print(saving)


    #2. calculate the total and hence the average
    total_saving = sum(saving)
    average_savings = total_saving / len(saving)
    print("======= Saving Analyser Report ========")
    print(f"  Total savings: ${total_saving:.2f}")
    print(f"Average savings: ${average_savings:.2f}")


if __name__ == "__main__":
    main()