class TeslaInterview:

    # codility.com demo task
    def first_missing_positive(self, nums: [int]) -> int:
        """
        Given an array of integers, find the first missing positive integer.
        In other words, find the lowest positive integer that does not exist in the array.
        The array can contain duplicates and negative numbers as well.
        For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
        You can modify the input array in-place.
        """
        nums_set = set()
        for num in nums:
            if num < 1:
                continue
            else:
                nums_set.add(num)
        for i in range(1, 500002):
            if i not in nums_set:
                return i
