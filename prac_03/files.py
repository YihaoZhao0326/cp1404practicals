FILENAME_FOR_1_and_2 = "name.txt"
FILENAME_FOR_3_and_4 = "numbers.txt"

# 1
out_name = input("Name: ")
out_file = open(FILENAME_FOR_1_and_2, 'w')
print(out_name, file=out_file)
out_file.close()

# 2
in_file = open(FILENAME_FOR_1_and_2)
in_name = in_file.read().strip()
print(f"Hi {in_name}!")
in_file.close()

# 3
with open(FILENAME_FOR_3_and_4) as in_file:
    total = 0
    for i in range(2):
        number = int(in_file.readline())
        total += number
    print(total)

# 4
with open(FILENAME_FOR_3_and_4) as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number
    print(total)
