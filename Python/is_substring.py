def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            return True
        index += 1
    return False


print(is_substring('bad', 'abracadabra'))
print(is_substring('dab', 'abracadabra'))