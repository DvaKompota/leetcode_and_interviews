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


    # codility.com demo task2
    def longest_binary_gap(self, num: int) -> int:
        """
        Find the longest binary gap in a given integer.
        """
        n_bin = bin(num)
        bin_str = str(n_bin)[2:]
        longest_gap = 0
        gap_length = 0
        gap_started = False
        gap_ended = False
        for i, digit in enumerate(bin_str):
            if gap_started and not gap_ended:
                if digit == '1':
                    gap_ended = True
                elif digit == '0':
                    gap_length += 1
            elif not gap_started and digit == '0':
                continue
            elif not gap_started and digit == '1':
                gap_started = True
            elif gap_started and digit == '1':
                gap_ended = True
                gap_started = False
            if gap_ended:
                longest_gap = gap_length if gap_length > longest_gap else longest_gap
                gap_length = 0
                if i + 1 < len(bin_str) and bin_str[i + 1] == '0':
                    gap_started = True
                gap_ended = False
        return longest_gap
