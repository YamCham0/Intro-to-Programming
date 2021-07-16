def locate_all(string, sub):
    index = 0
    matches = []
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches

# Here are a couple function calls to test with.
# This one should return 1
print(locate_all('cookbook', 'ook'))
# This one should return -1
print(locate_all('all your bass are belong to us', 'base'))
