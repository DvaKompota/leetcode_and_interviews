# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?

# You are given an array of integers. Please return sum of all elements
# [5, 1, 10, 24, -4, 10, 5, 3, 6, 7, 0, 20, 30]  ----> n elements

class SumElementsInArray:

    def sum_elements(self, arr):
        if len(arr) == 0:
            return "Array is empty!"
        total = 0
        for item in arr:
            total += item
        return total
    # RUNTIME: 0(n)
    # MEMORY: 0(1)
