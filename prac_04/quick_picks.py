from random import randint
RANDOM_NUMBERS_NUMBER = 6
MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45
quick_pick_number = int(input("How many quick picks? "))
for i in range(quick_pick_number):
    numbers = []
    for j in range(RANDOM_NUMBERS_NUMBER):
        number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        while number in numbers:
            number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        numbers.append(number)
    numbers.sort()
    for number in numbers:
        print(f"{number:>2}", end=" ")
    print()
