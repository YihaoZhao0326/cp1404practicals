PASSWORD_LENGTH = 6


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("password: ")
    while len(password) < PASSWORD_LENGTH:
        print(f"Your password shouldn't less than {PASSWORD_LENGTH}")
        password = input("password: ")
    return password


main()
