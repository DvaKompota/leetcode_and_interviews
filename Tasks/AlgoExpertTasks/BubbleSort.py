#   Write a function that takes in an array of integers and returns a sorted
#   version of that array. Use the Bubble Sort algorithm to sort the array.
#
#   Sample Input:
#   array = [8, 5, 2, 9, 5, 6, 3]
#
#   Sample Output:
#   [2, 3, 5, 5, 6, 8, 9]


def bubble_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    for right in range(len(array) - 1, 0, -1):
        had_swaps = False
        for i in range(0, right):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                had_swaps = True
        if not had_swaps:
            return array
    return array
