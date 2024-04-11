from collections import Counter

#the problem statement given here.

#Given two arrays A1[] and A2[], sort A1 in such a way that the
# relative order among the elements will be same as those are in A2.
# For the elements not present in A2, append them at last in sorted order.

#Example:

#Input: A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
#       A2[] = {2, 1, 8, 3}
#Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}


# Function to sort arr1
# according to arr2
def solve(arr1, arr2):
    # Our output array
    res = []

    # Counting Frequency of each
    # number in arr1
    f = Counter(arr1)

    # Iterate over arr2 and append all
    # occurrences of element of
    # arr2 from arr1
    for e in arr2:
        # Appending element 'e',
        # f[e] number of times
        res.extend([e] * f[e])

        # Count of 'e' after appending is zero
        f[e] = 0

    # Remaining numbers in arr1 in sorted
    # order (Numbers with non-zero frequency)
    rem = list(sorted(filter(
        lambda x: f[x] != 0, f.keys())))

    # Append them also
    for e in rem:
        res.extend([e] * f[e])

    return res


# Driver Code
if __name__ == "__main__":
    arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    arr2 = [2, 1, 8, 3]
    print(*solve(arr1, arr2))