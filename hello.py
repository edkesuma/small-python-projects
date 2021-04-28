# This program asks for the user's name and age
print("Hello there! What's your name?")
name = input("Name: ")
print("It's good to meet you, " + name)
length_of_name = len(name)
print("Your name is " + str(length_of_name) + " characters long")
print("What is your age?")
age = input("Age: ")
print("Your age will be " + str(int(age)+1) + " in a year's time!")
