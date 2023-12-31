def longestPalindrome(string: str) -> str:
    n = len(string)  # calculating size of string
    if (n < 2):
        return n  # if string is empty then size will be 0.
        # if n==1 then, answer will be 1(single
        # character will always palindrome)
    start = 0
    maxLength = 1
    for i in range(n):
        low = i - 1
        high = i + 1
        while (high < n and string[high] == string[i]):
            print(f"high is {string[high]} string i is {string[i]}")
            high = high + 1

        while (low >= 0 and string[low] == string[i]):
            print(f"low is {string[low]} string i is {string[i]}")
            low = low - 1

        while (low >= 0 and high < n and string[low] == string[high]):
            low = low - 1
            high = high + 1

        length = high - low - 1
        if (maxLength < length):
            maxLength = length
            start = low + 1

    print("Longest palindrome substring is:", end=" ")
    print(string[start:start + maxLength])

    return maxLength
# babad b,b

if __name__ == '__main__':
    first_result = longestPalindrome("tacocat")
    second_result = longestPalindrome("not")
    fourth_result = longestPalindrome("cbbd")

