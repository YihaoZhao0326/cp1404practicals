import random


def main():
    """ask a score and print the grade, then random generate a score and print the grade"""
    score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(grade)
    score = random.randint(0, 100)
    grade = determine_grade(score)
    print(f"random score: {score}\ngrade: {grade}")


def determine_grade(score):
    """determine grade base on the input score"""
    if score < 0 or score > 100:
        message = "Invalid score"
    elif score < 50:
        message = "Bad"
    elif score < 90:
        message = "Passable"
    else:
        message = "Excellent"
    return message


main()
