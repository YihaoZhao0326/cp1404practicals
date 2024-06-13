for i in range(1, 21, 2):
    print(i, end=' ')
print()

# question a
print("Question a:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# question b
print("Question b:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# question c
print("Question c:")
number = int(input("Number of stars: "))
for i in range(number):
    print("*", end='')
print()

# question d
print("Question d:")
for i in range(number):
    for j in range(i + 1):
        print("*", end='')
    print()
