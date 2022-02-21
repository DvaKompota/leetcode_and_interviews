# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?
#
# Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class TwoSum:

    def twoSumIndex(self, arr=None, target=None):
        for x in arr:
            try:
                y = arr.index(target - x, arr.index(x)+1)
                if y == arr.index(x):
                    pass
                else:
                    return [arr.index(x), y]
            except:
                pass
        return "There are no matching numbers"

    def twoSum(self, nums: [int], target: int) -> [int]:
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = i
        for i in range(0, len(nums)):
            num1 = nums[i]
            num2 = target - num1
            if num2 in d and i != d[num2]:
                return [i, d[num2]]
        return "There are no matching numbers"
    # RUNTIME: 0(n)
    # MEMORY: 0(1)
