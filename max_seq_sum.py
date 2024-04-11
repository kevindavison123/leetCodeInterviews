def maxSumIS(Arr, n):
    dp = [-1] * (n + 1)

    def solve(Arr, i, n, dp):
        if i == n:
            return 0
        if dp[i] != -1:
            return dp[i]

        result = Arr[i]
        for j in range(i + 1, n):
            if Arr[i] < Arr[j]:
                result = max(result, Arr[i] + solve(Arr, j, n, dp))
        dp[i] = result
        return dp[i]

    result = 0
    for i in range(n):
        result = max(result, solve(Arr, i, n, dp))
    return result


if __name__ == '__main__':
   print(maxSumIS([1,101,2,3,100], 5))
   print(maxSumIS([9,4,8,3,2], 5))