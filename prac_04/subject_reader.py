"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    datas = load_data()
    print(datas)
    max_name_length = max(len(data[1]) for data in datas)
    max_number_length = max(len(str(data[2])) for data in datas)
    for data in datas:
        print(f"{data[0]} is taught by {data[1]:{max_name_length}} and has {data[2]:{max_number_length}} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    datas = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        datas.append(parts)
        # print(parts)  # See if that worked
        # print("----------")
    input_file.close()
    return datas


main()