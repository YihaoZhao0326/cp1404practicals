"""
CP1404/CP5632 - Practical
Broken program to determine score status
get score
if score < 0 or score > 100
    print invalid
else if score < 50
    print bad
else if score < 90
    print pass
else
    print excellent
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:
    message = "Invalid score"
elif score < 50:
    message = "Bad"
elif score < 90:
    message = "Passable"
else:
    message = "Excellent"
print(message)
