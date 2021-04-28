# Guess the number game
import random
secret_number = random.randint(0,100)
print("I am thinking of a number between 0 and 100.")
guess_counter = 0
keep_going = True
while(keep_going):
    print("Take a guess.")
    guessed_number = int(input("Number: "))
    guess_counter += 1
    if (guessed_number > secret_number):
        print("Your guess is too high.")
        continue
    elif (guessed_number < secret_number):
        print("Your guess is too low.")
        continue
    else:
        print("Good job! You guessed my number in " + str(guess_counter) + " guesses")
        keep_going = False
