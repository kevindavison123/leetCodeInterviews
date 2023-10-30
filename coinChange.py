from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    coins.sort(reverse=True)
    number_of_coins = 0
    pointer = 0
    size = len(coins)

    while amount > 0:
        if pointer+1 > size:
            return -1
        if coins[pointer] <= amount:
            number_of_coins = number_of_coins + 1
            amount = amount - coins[pointer]
        else:
            pointer = pointer + 1
    return number_of_coins


if __name__ == '__main__':
    first_result = coinChange([1, 2, 5], 11)
    second_result = coinChange([3], 2)
    third_result = coinChange([1], 0)
    print(first_result)
    print(second_result)
    print(third_result)