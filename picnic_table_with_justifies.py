# picnic table with ljust, rjust and center with dictionaries
def print_picnic(item_dict, left_width, right_width):
    print("PICNIC ITEMS".center(left_width + right_width, "-"))
    for key, value in item_dict.items():
        print(key.ljust(left_width, ".") + str(value).rjust(right_width))

picnic_items = {"sandwiches": 4, "apples": 12, "cups": 4, "cookies": 8000}
print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)
