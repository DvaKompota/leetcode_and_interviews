#   Write a function that takes in a non-empty array of distinct integers and an
#   integer representing a target sum. If any two numbers in the input array sum
#   up to the target sum, the function should return them in an array, in any
#   order. If no two numbers sum up to the target sum, the function should return
#   an empty array.
#
#   Note that the target sum has to be obtained by summing two different integers
#   in the array; you can't add a single integer to itself in order to obtain the
#   target sum.
#
#   You can assume that there will be at most one pair of numbers summing up to
#   the target sum.

#   Sample Input:
#   array = [3, 5, -4, 8, 11, 1, -1, 6]
#   targetSum = 10

#  Sample Output:
#   [-1, 11] // the numbers could be in reverse order


def two_number_sum(array: [int], target_sum: int) -> [int]:
    """
    :param array:       [int] - an array of integers
    :param target_sum:  int - the target sum

    :return:            [int] - an array of two integers that sum to the target sum
    """
    d = []
    for i, num in enumerate(array):
        if target_sum - num in d:
            return [target_sum - num, num]
        else:
            d.append(num)
    return []
