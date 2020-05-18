# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?
#
# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
# Do not return anything, modify nums in-place instead.


class MoveZeroes:
    def moveZeroes(self, nums: [int]) -> None:
        write_pointer = 0
        for read_pointer in range(0, len(nums)):
            if nums[read_pointer] != 0:
                nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
                write_pointer += 1



# class MoveZeroes:
#     def moveZeroes(self, nums: [int]) -> None:
#         write_pointer = 0
#         for read_pointer in range(0, len(nums)):
#             if nums[read_pointer] != 0:
#                 nums[write_pointer] = nums[read_pointer]
#                 write_pointer += 1
#
#         for i in range(write_pointer, len(nums)):
#             nums[i] = 0
