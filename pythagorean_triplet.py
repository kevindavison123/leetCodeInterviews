# Given an array of integers, write a function that returns true if
# there is a triplet (a, b, c) that satisfies a2 + b2 = c2.
import math


# Hashing, we want to put all the inputs into a hash
def pythagorean_triplet(input_arr):
    input_size = len(input_arr)
    maximum = max(input_arr)
    hash = [0]*(maximum+1)

    for i in range(input_size):
        input_elem = input_arr[i]
        hash[input_elem] += 1
    for i in range(1, maximum+1):
        if (hash[i] == 0):
            continue
        for j in range(1, maximum+1):
            #If a and b are the same and there is only one or there is no b in original array
            if ((i == j and hash[i] == 1) or hash[j] == 0):
                continue
            # find c
            c_value = int(math.sqrt(i * i + j * j))
            if ((c_value * c_value) != (i * i + j * j )):
                continue
            if (c_value > maximum):
                continue
            if (hash[c_value]):
                return c_value
    return None

if __name__ == '__main__':
    print(pythagorean_triplet([3, 1, 4, 6, 5]))
    print(pythagorean_triplet([10, 4, 6, 12, 5]))
    print(pythagorean_triplet([0, 1, 1, 8, 12]))