#   Given an array of positive integers representing the values of coins in your
#   possession, write a function that returns the minimum amount of change (the
#   minimum sum of money) that you cannot create. The given coins can have
#   any positive integer value and aren't necessarily unique (i.e., you can have
#   multiple coins of the same value).
#
#   For example, if you're given coins = [1, 2, 5], the minimum
#   amount of change that you can't create is 4. If you're given no
#   coins, the minimum amount of change that you can't create is 1.
#
#   Sample Input:
#   coins  = [5, 7, 1, 1, 2, 3, 22]
#
#   Sample Output:
#   20


def non_constructible_change(coins):

    if not coins:
        return 1

    coins.sort()
    if coins[0] != 1:
        return 1
    if len(coins) == 1:
        return coins[0] + 1
    current_sum = coins[0]
    for coin in coins[1:]:
        if coin > current_sum + 1:
            return current_sum + 1
        current_sum += coin
    return current_sum + 1
