"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        message = "Hello " + name
    elif choice == "G":
        message = "Goodbye " + name
    else:
        message = "Invalid choice"
    print(message)
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
