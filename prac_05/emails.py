"""
Emails
estimate :30
actual   :11
"""

email_to_name = {}
e_mail = input("Email: ")
while e_mail != "":
    generate_name = e_mail.split("@")[0].replace(".", " ").title()
    ask_name_or_not = input(f"Is your name {generate_name}? （Y/n) ").upper()
    if ask_name_or_not == "Y" or ask_name_or_not == "":
        name = generate_name
    else:
        name = input("Name: ")
    email_to_name[e_mail] = name
    e_mail = input("Email: ")
print()
for key in email_to_name:
    print(f"{email_to_name[key]} ({key})")
