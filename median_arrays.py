#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
import math
from typing import List


#The overall run time complexity should be O(log (m+n)).


#Example 1:

#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.
#
#Example 2:
#
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


def findMedianSortedArrays(nums1: List[int], nums2: List[int]):
    results = sorted(nums1 + nums2)
    size = len(results)
    if size % 2 == 0:
        position_1 = math.floor(size/2)
        position_2 = math.ceil(size/2-1)
        return (results[position_1] + results[position_2]) / 2
    else:
        return results[int(size / 2)]



if __name__ == '__main__':
    print(findMedianSortedArrays([1,3], [2]))
    print(findMedianSortedArrays([1,2], [3,4]))
    print(findMedianSortedArrays([1,2,5], [3,4]))
    print(findMedianSortedArrays([1,2,5], [3,4,6]))
