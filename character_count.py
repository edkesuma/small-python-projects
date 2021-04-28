# count the number of characters in a string with a dictionary
import pprint

message = "This is a random string I came up with."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(pprint.pformat(count))
