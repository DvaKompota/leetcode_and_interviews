# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?
#
# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.


class Sortings:

    def bubble_sort(self, nums: [int]):
        swap_detected = True
        while swap_detected is True:
            swap_detected = False
            for i in range(len(nums)-1):
                if nums[i+1] < nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swap_detected = True
        return nums
    # RUNTIME: 0(n^2)
    # MEMORY: 0(1)

    def selection_sort(self, nums: [int]):
        for left in range(len(nums)):
            min_index = left
            for i in range(left, len(nums)):
                if nums[i] < nums[min_index]:
                    min_index = i
            nums[left], nums[min_index] = nums[min_index], nums[left]
        return nums
    # RUNTIME: 0(n^2)
    # MEMORY: 0(1)

    def counting_sort(self, nums: [int]):
        max_value = 0
        for num in nums:
            if num < 0:
                return "Counting sorting does not support negative integers"
            if num > max_value:
                max_value = num

        values = [0]*(max_value + 1)
        for num in nums:
            values[num] += 1
        k = 0
        for i in range(max_value + 1):
            for j in range(values[i]):
                nums[k] = i
                k += 1
        return nums
    # RUNTIME: 0(n)
    # MEMORY: 0(n*max_value)

