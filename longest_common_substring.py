
# Given two strings. The task is to find the length of the longest common substring.
# Example 1:
#
# Input: S1 = "ABCDGH", S2 = "ACDGHR", n = 6, m = 6
# Output: 4
# Explanation: The longest common substring
# is "CDGH" which has length 4.
#
# Example 2:
#
# Input: S1 = "ABC", S2 "ACB", n = 3, m = 3
# Output: 1
# Explanation: The longest common substrings
# are "A", "B", "C" all having length 1.
def longestCommonSubstr(S1, S2, n, m):
    dp = [[0 for i in range( m +1)] for i in range( n +1)]

    res = 0

    for i in range(1, n+ 1):
        for j in range(1, m + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 0

            res = max(res, dp[i][j])

    return res


if __name__ == '__main__':
    print(longestCommonSubstr("ABCDGH", "ACDGHR", 6, 6))
    print(longestCommonSubstr("ABC", "ACB", 3, 3))