#   Write a function that takes in a sorted array of integers as well as a target
#   integer. The function should use the Binary Search algorithm to determine if
#   the target integer is contained in the array and should return its index if it
#   is, otherwise -1.
#
#   Sample Input:
#   array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
#   target = 33
#
#   Sample Output:
#   3


def binary_search(array, target):
    left = 0
    right = len(array) - 1
    mid = int((right + left) / 2)
    for i in range(int(len(array) / 2)):
        if array[left] == target:
            return left
        if array[right] == target:
            return right
        if array[mid] == target:
            return mid
        if mid <= left or mid >= right:
            return -1
        right = mid - 1 if array[mid] > target else right
        left = mid + 1 if array[mid] < target else left
        mid = int((right + left) / 2)
    return -1


def recursive_binary_search(array, target):

    def _recursive_binary_search(_array, _target, left, right):
        mid = int((right + left) / 2)
        if _array[left] == target:
            return left
        if _array[right] == target:
            return right
        if _array[mid] == target:
            return mid
        if mid <= left or mid >= right:
            return -1
        if _array[mid] > target:
            return _recursive_binary_search(_array, _target, left, mid - 1)
        if _array[mid] < target:
            return _recursive_binary_search(_array, _target, mid + 1, right)
        return -1

    return _recursive_binary_search(array, target, 0, len(array) - 1)
