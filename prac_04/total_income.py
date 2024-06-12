"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month = int(input("How many months? "))

    for month in range(1, month + 1):
        # income = float(input("Enter income for month " + str(month) + ": "))
        income = float(input(f"Enter income for month {month}:"))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """this function input a list of income and print a well form report"""
    print("\nIncome Report\n-------------")
    total = 0
    for i in range(len(incomes)):
        income = incomes[i]
        total += income
        print(f"Month {i + 1:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
