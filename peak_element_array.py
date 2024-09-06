def find_peak_in_array(size, arr):
    if size == 1:
        return 0
    if size == 2:
        return 0 if arr[0] >= arr[1] else 1
    for i in range(size):
        if i == 0:
            if arr[i] >= arr[i+1]:
                return i
        elif i == size - 1:
            if arr[i] >= arr[i-1]:
                return i
        elif arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                return i
    return -1


def find_min_max_array(arr):
    min_element = arr[0]
    max_element = arr[0]
    if len(arr) == 1:
        return min_element, max_element
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
        if arr[i] > max_element:
            max_element = arr[i]




if __name__ == '__main__':
    arr = [1, 3, 20, 4, 1, 0]
    size = len(arr)
    print(find_peak_in_array(size, arr))
    print(find_min_max_array(arr))