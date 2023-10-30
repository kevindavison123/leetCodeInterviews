from typing import List

# Cost of 0, 1 is nothing
# Ensure we get to the top with steps + 1
# calculate the minimum cost of reaching current step
# this can be done by either taking one step back or two steps forward
#

def minCostClimbingStairs(cost: List[int]) -> int:
    print(cost)
    length_of_stairs = len(cost)
    the_top = length_of_stairs + 1
    #init array of costs
    prices = [0] * (length_of_stairs+2)
    #init first and second step
    prices[1] = 0
    prices[2] = 0
    for i in range (3, the_top+1):
        print(f"min {cost[i-3]} + {prices[i-2]}, {cost[i-2]} + {prices[i-1]}")
        prices[i] = min(cost[i - 3] + prices[i - 2 ], cost[i - 2] + prices[i - 1])
        print(prices[i])
    print(prices[the_top])
    return prices[the_top]






if __name__ == '__main__':
    # first_result = minCostClimbingStairs([10,15,20])
    # second_result = minCostClimbingStairs([1,100,1,1,100,1])
    third_result = minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
