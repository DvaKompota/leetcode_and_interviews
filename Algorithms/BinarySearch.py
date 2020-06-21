# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?
#
# given an array of integers and target
# find the location of target
#
# [10, -39, 100, 3, 6, 19, 2]; target = 19

class BinarySearch:

    def search_an_element(self, nums: [int], target: int):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    # RUNTIME: 0(n)
    # MEMORY: 0(1)

    # what if the array is sorted? [-39, 2, 3, 6, 10, 19, 100]
    # mid element = 6
    # 19 > 6 => target is in the right part [10, 19, 100]
    # mid element = 19 == target => found!

    def binary_search(self, nums: [int], target: int):
        return self.binary_search_recursion(nums, target, 0, len(nums)-1)

    def binary_search_recursion(self, nums: [int], target: int, left: int, right: int):
        middle_index = int((left + right) / 2)
        if right < left:
            return -1
        if nums[middle_index] == target:
            return middle_index
        elif target < nums[middle_index]:
            new_right = middle_index - 1
            return self.binary_search_recursion(nums, target, left, new_right)
        else:
            new_left = middle_index + 1
            return self.binary_search_recursion(nums, target, new_left, right)
    # RUNTIME: 0(log n)
    # MEMORY: 0(1)
