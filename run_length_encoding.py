
# aaabbccc
# 3a2b3c
def encode(encoded_string):
    # check for null
    if encoded_string is None:
        return ""
    result = ""
    counter = 0
    prev_char = 0
    for char in encoded_string:
        if char == prev_char:
            counter += 1
        else:
            if prev_char != 0:
                result += str(counter) + str(prev_char)
            prev_char = char
            counter = 1
    result += str(counter) + str(prev_char)
    return result






if __name__ == '__main__':
    print(encode("aaabbccc"))
    print(encode("aaaaaaaaaaaaaaaaaaaa"))
    print(encode("abcd"))
