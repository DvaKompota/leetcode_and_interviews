#   Write a function that takes in a non-empty array of integers that are sorted
#   in ascending order and returns a new array of the same length with the squares
#   of the original integers also sorted in ascending order.
#
#   Sample Input:
#   array = [1, 4, 9, 25, 36, 64, 81]
#
#   Sample Output:
#   [1, 4, 9, 25, 36, 64, 81]


def sorted_squared_array(array):
    output = []
    left = 0
    right = len(array) - 1
    for i in range(len(array)):
        if abs(array[left]) >= abs(array[right]):
            output.insert(0, array[left]**2)
            left += 1
        else:
            output.insert(0, array[right]**2)
            right -= 1
        if left > right:
            break
    return output
