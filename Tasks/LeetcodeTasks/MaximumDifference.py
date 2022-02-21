# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?

# Given an array of integers, return the difference between
# the largest and smallest integers in the array.

class MaximumDifference:

    def maximum_difference(self, nums: [int]):
        min_value = max_value = nums[0]
        for num in nums:
            if num < min_value:
                min_value = num
            if num > max_value:
                max_value = num
        return max_value - min_value
    # RUNTIME: 0(n)
    # MEMORY: 0(1)
