def count_character(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total

# This should return 3, since there are three "o"s:
print(count_character("bonobo", "o"))