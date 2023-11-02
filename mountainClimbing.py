# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """

def findInMountainArray( mountain_arr: list, target: int) -> int:
    length = len(mountain_arr)
    peak_index = find_peak(0, length - 1, mountain_arr)
    print(f"peak: {peak_index}")
    climbing_idx = binary_search(0, peak_index, target, mountain_arr, False)
    print(f"climbing_idx: {climbing_idx}, target: {target}, mountain_arr: {mountain_arr[climbing_idx]}")
    if mountain_arr[climbing_idx] == target:
        return climbing_idx
    descending_idx = binary_search(peak_index + 1, length - 1, target, mountain_arr, True)
    print(f"descending_idx: {descending_idx}, target: {target}, mountain_arr: {mountain_arr[descending_idx]}")
    if mountain_arr[descending_idx] == target:
        return descending_idx
    print("Could not find. -1")
    return -1


def find_peak(low, high, mountain_arr):
    while low != high:
        mid = low + (high - low) // 2
        if mountain_arr[mid] < mountain_arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low


def binary_search( low, high, target, mountain_arr, reversed):
    while low != high:
        mid = low + (high - low) // 2
        if reversed:
            if mountain_arr[mid] > target:
                low = mid + 1
            else:
                high = mid
        else:
            if mountain_arr[mid] < target:
                low = mid + 1
            else:
                high = mid
    return low

if __name__ == '__main__':
    first_result = findInMountainArray([1, 2, 3, 4, 5, 3, 1], 3)
    second_result = findInMountainArray([0, 1, 2, 4, 2, 1], 3)
    third_result = findInMountainArray([1, 5, 2], 2)
    fourth_result = findInMountainArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
     90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85,
     84, 83, 82],  81)





