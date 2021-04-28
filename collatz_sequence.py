# collatz sequence
def collatz(users_number):
    if (users_number % 2 == 0):
        answer = users_number // 2
    elif (users_number % 2 == 1):
        answer = users_number * 3 + 1
    print(answer)

try:
    print("Enter number: ")
    users_input = input()
    users_number = int(users_input)
    collatz(users_number)
except ValueError:
    print("Enter integer la blyad.")
