PASSWORD_LENGTH = 6


def main():
    """get a valid password and convert it to asterisks"""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """convert password to asterisks"""
    print("*" * len(password))


def get_password():
    """get a valid password which length is greater than PASSWORD_LENGTH"""
    password = input("password: ")
    while len(password) < PASSWORD_LENGTH:
        print(f"Your password shouldn't less than {PASSWORD_LENGTH}")
        password = input("password: ")
    return password


main()
