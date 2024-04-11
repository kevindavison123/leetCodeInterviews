# You are given a set of N types of rectangular 3-D boxes, where the ith box
# has height h, width w and length l. Your task is to create a stack of boxes
# which is as tall as possible, but you can only stack a box on top of another box
# if the dimensions of the 2-D base of the lower box are each strictly larger than
# those of the 2-D base of the higher box. Of course, you can rotate a box so that
# any side functions as its base.It is also allowable to use multiple instances of
# the same type of box. Your task is to complete the function maxHeight which returns
# the height of the highest possible stack so formed.
def box_stacking(n: int, height: [], width: [], length: []):
    dp = [0 for i in range(10005)]
    rotated = []
    for i in range(n):
        a = height[i]
        b = width[i]
        c = length[i]
        rotated.append([[a, b], c])
        rotated.append([[b, a], c])
        rotated.append([[a, c], b])
        rotated.append([[c, a], b])
        rotated.append([[c, b], a])
        rotated.append([[b, c], a])
        rotated.sort()
    rotated.sort()
    for i in range(len(rotated)):
        dp[i] = rotated[i][1]
        for j in range(i):
            if rotated[i][0][0] > rotated[j][0][0] and rotated[i][0][1] > rotated[j][0][1]:
                dp[i] = max(dp[i], dp[j] + rotated[i][1])
    return max(dp)


if __name__ == '__main__':
    print(box_stacking(4, [4, 1, 4, 10], [6, 2, 5, 12], [7, 3, 6, 32]))
    print(box_stacking(3, [1, 4, 3], [2, 5, 4], [3, 6, 1]))
