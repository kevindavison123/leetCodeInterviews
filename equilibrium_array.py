#Given an array arr[] of size n, return an equilibrium index (if any) or -1 if no equilibrium index exists. The equilibrium index of an array is an index such that the sum of elements at lower indexes equals the sum of elements at higher indexes.

# Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.

# Examples:

# Input: arr[] = {-7, 1, 5, 2, -4, 3, 0}
# Output: 4
# Explanation: In 1-based indexing, 4 is an equilibrium index, because: arr[1] + arr[2] + arr[3] = arr[5] + arr[6] + arr[7]
#
# Input: arr[] = {1, 2, 3}
# Output: -1
# Explanation: There is no equilibrium index in the array.

def findEquilibrium(arr):
    n = len(arr)
    #find prefix and suffic sums
    prefix_sum = [0] * n
    suffix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    suffix_sum[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix_sum[i] = suffix_sum[i+1] + arr[i]
    #find equilibrium index
    print(prefix_sum, suffix_sum)
    for i in range(n):
        if prefix_sum[i] == suffix_sum[i]:
            return i+1
    return -1


if __name__ == '__main__':
    arr = [-7, 1, 5, 2, -4, 3, 0]
    print(findEquilibrium(arr))


