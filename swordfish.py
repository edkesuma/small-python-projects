# A program to check for password and practice loops
while True:
    print("Who are you?")
    name = input("Name: ")
    if (name != "Joe"):
        continue
    print("What the password blyad. It do be a fish.")
    password = input("Password: ")
    if (password == "swordfish"):
        break
print("Access granted")
