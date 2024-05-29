"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sale
while sale > 0
    if sale < 1000
        bonus = sale * 0.1
    else
        bonus = sale * 0.15
    print bonus
    get sale
"""
BONUS_THRESHOLD = 1000
LOW_BONUS = 0.1
HIGH_BONUS = 0.15

sale = float(input("Enter sales: $"))
while sale >= 0:
    if sale < BONUS_THRESHOLD:
        bonus = sale * LOW_BONUS
    else:
        bonus = sale * HIGH_BONUS
    print(f"Your bonus is: {bonus}$")
    sale = float(input("Enter sales: $"))
