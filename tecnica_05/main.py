string = input("Enter a string: ")


# Simple solution
# This function invert letters of word and the order of the words
def inverte_string_v1(string):
    return string[::-1]


res = inverte_string_v1(string)
print(f'Version 1\n{res}\n')  # Output: "dlrow olleH"


# This function invert letters of word and the order of the words
def inverte_string_v2(string):
    length = len(string)
    inverted_string = ""

    for i in range(length - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string


res = inverte_string_v2(string)
print(f'Version 2\n{res}\n')  # Output: "dlrow olleH"


# This function invert letters of word but not the order of the words
def inverte_string_v3(string):
    worlds = string.split(" ")
    inverted_string = [world[::-1] for world in worlds]

    return " ".join(inverted_string)


res = inverte_string_v3(string)
print(f'Version 3\n{res}\n')  # Output: "olleH dlrow"
