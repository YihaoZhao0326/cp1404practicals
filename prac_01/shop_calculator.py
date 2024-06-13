"""
total = 0
get number
while number < 0
    print invalid message
    get number
repeat number times
    get price
    total = total + price
if total > 100
    total = total * (1 - 0.1)
print total
"""
DISCOUNT_THRESHOLD = 100
DISCOUNT = 0.1
total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = input("Number of items: ")
for i in range(number):
    price = float(input("Price of item: "))
    total += price
if total > DISCOUNT_THRESHOLD:
    total *= (1 - DISCOUNT)
print(f"Total price for 3 items is ${total:.2f}")
