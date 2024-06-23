NAME_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc"}
max_key_length = max(len(key) for key in NAME_TO_CODE)
for key in NAME_TO_CODE:
    print(f"{key:{max_key_length}} is {NAME_TO_CODE[key]}")

color_name = input("Enter color name: ").lower()

while color_name != "":
    try:
        print(color_name, "is", NAME_TO_CODE[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").lower()
