def read_data(filename):
    """Read from csv file and put into a list of lists."""
    student_scores = []
    file_in = open(filename, "r")
    for line in file_in:

        line = line.strip()          # remove newline
        line = line.replace('"', '') # remove quotation marks

        student_data = line.split(",")

        # student_data[1] = float(student_data[1])
        # student_data[2] = float(student_data[2])
        # student_data[3] = float(student_data[3])

        for i in range(1,4):
            student_data = float(student_data[i])



        student_scores.append(student_data)

    file_in.close()
    return student_scores

def display_scores(student_scores):

    print("---- Average Score of each Student ----")
    for score in student_scores:
        total = score[1] +score[2] + score[3]
        average = total / 3
        print(f"{score[0]} scored {average:.1f}")


def main():
    student_scores = []
    #1. read the database into a list of lists
    student_scores = read_data("student_scores.csv")
    print(student_scores) #debugging
    print()
    print()

    #2. display student average scores nicely
    display_scores(student_scores)


if __name__ == "__main__":
    #this will be executed when this file is run
    main()