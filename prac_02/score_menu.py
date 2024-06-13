LOWEST_SCORE = 0
HIGHEST_SCORE = 100
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """a menu that can get a valid score, print grade based on score and print stars based on score"""
    score = get_valid_score()
    print(MENU)
    choice = input("choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            grade = determine_grade(score)
            print(grade)
        elif choice == "S":
            print_stars(score)
        else:
            print("invalid choice")
        print(MENU)
        choice = input("choice: ").upper()
    print("farewell")


def print_stars(score):
    """print number of score's star"""
    print("*" * score)


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


def get_valid_score():
    """get a score between LOWEST_SCORE and HIGHEST_SCORE"""
    score = int(input("score: "))
    while score < LOWEST_SCORE or score > HIGHEST_SCORE:
        print("invalid score")
        score = int(input("score: "))
    return score


main()
