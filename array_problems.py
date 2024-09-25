
def equilibrium_index_of_array(arr):
    size = len(arr)
    left_sum = 0
    right_sum = sum(arr[1:])
    pivot = 0
    while pivot < size - 1 and right_sum != left_sum:
        left_sum += arr[pivot]
        right_sum -= arr[pivot + 1]
        pivot += 1
    return pivot + 1 if left_sum == right_sum else -1




if __name__ == '__main__':
    arr = [-7, 1, 5, 2, -4, 3, 0]
    print(equilibrium_index_of_array(arr))