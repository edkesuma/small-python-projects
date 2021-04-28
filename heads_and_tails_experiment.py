# random heads and tails program
import random
num_of_streaks = 0
space_for_list = []
heads_counter = 0
tails_counter = 0

for experiment_number in range(10000):
    # code that creates a list of 100 heads or tails values
    if (random.randint(0,1) == 0):
        space_for_list.append("H")
    else:
        space_for_list.append("T")
    # code that checks if there is a streak of 6 heads or tails in a row
    if (space_for_list[experiment_number] == "H"):
        heads_counter += 1
        tails_counter = 0
    elif(space_for_list[experiment_number] == "T"):
        tails_counter += 1
        heads_counter = 0

    if (heads_counter >= 6 or tails_counter >= 6):
        num_of_streaks += 1

print("Chance of streak: %s%%" % (num_of_streaks/100))
