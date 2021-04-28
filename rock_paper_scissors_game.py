import random
import sys
import time

# time module not from original problem example

# Rock paper scissors game
print("ROCK, PAPER, SCISSORS")

# variables to hold num of wins, losses and ties
wins = 0
losses = 0
ties = 0

# main loop
while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    # prompt to user
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input("What will it be: ")
        if (player_move == "q"):
            sys.exit()
        if (player_move == "r" or player_move == "p" or player_move == "s"):
            break
        print("Type r, p, s or q")

    # print stuff to user
    if (player_move == "r"):
        print("ROCK versus...")
    if (player_move == "p"):
        print("PAPER versus...")
    if (player_move == "s"):
        print("SCISSORS versus...")
    time.sleep(2)

    # randomizer for computer move
    computer_move = random.randint(1,3)
    if (computer_move == 1):
        computer_move = "r"
        print("ROCK")
    if (computer_move == 2):
        computer_move = "p"
        print("PAPER")
    if (computer_move == 3):
        computer_move = "s"
        print("SCISSORS")
    time.sleep(1)

    # seeing who wins
    if (computer_move == player_move):
        print("It's a tie!")
        ties += 1
    elif (player_move == "r" and computer_move == "s"):
        print("You win!")
        wins += 1
    elif (player_move == "s" and computer_move == "p"):
        print("You win!")
        wins += 1
    elif (player_move == "p" and computer_move == "r"):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1
    time.sleep(1)
