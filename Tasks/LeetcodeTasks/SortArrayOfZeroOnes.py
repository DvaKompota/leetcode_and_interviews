# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?

# Given an array of integers.
# All elements are either ones or zeros inside the array. Your goal is to order the array in ascending order.


class SortArrayOfZeroOnes:

    def sort_array_of_zero_ones(self, nums: [int]):
        count = 0
        for item in nums:
            if item != 0 and item != 1:
                return "Array contains invalid items!"
            count += item
        return [0]*(len(nums)-count)+[1]*count

    # RUNTIME: 0(n)
    # MEMORY: 0(1)
