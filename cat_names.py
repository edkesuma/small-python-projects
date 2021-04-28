# cat names with list
cat_names = []
while True:
    print("Enter the name of cat " + str(len(cat_names)+1) + " (Or enter nothing to stop.):")
    cat_input = input()
    cat_names = cat_names + [cat_input]
    if (cat_input == ""):
        break

print("The cat names are:")
for cat in cat_names:
    print(" " + cat)
