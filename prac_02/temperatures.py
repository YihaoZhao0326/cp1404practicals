MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit "


def main():
    """a menu that can convert celsius to fahrenheit or vice versa"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit):
    """convert input fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    """convert input celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


# main()
nums1 = [1, -5, 2, 0, 4, 2, -3]
nums2 = [1, -5, 2, 4, 4, 2, 7]
result = 0
j = 0
while j < len(nums1):
    if nums1[j] != nums2[j]:
        result = result + 1
    j = j + 1
print(result)