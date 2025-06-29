import re


class CodilityTasks:

    # demo task
    def first_missing_positive(self, nums: list[int]) -> int:
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

    # demo task 2
    def longest_binary_gap(self, num: int) -> int:
        """
        Find the longest binary gap in a given integer.

        A binary gap within a positive integer num is any maximal sequence of consecutive zeros
        that is surrounded by ones at both ends in the binary representation of num.
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

    # Tesla Online Coding Assessment – https://app.codility.com/public-link/Tesla-Qa-Automation---Sr-CR--2-2021-1/
    # task1
    def array_of_unique_integers_with_zero_sum(self, n: int) -> list[int]:
        """
        Return an array with length equal to n, that consists of unique integers with zero-sum.

        Array of integers with zero-sum means that the sum of all elements in the array is zero.
        """
        if n == 1:
            return [0]
        solution = []
        if n % 2 != 0:
            solution.append(0)
        for i in range(1, n//2+1):
            solution.append(-i)
            solution.append(i)
        return solution

    # task2
    def get_success_rate(self, tests: list[str], results: list[str]) -> int:
        """
        Return the success rate of the tests, given 2 arrays of strings, containing tests names and their results.

        Tests array contains unique tests names, consisting of parts: module name, test group number and test letter.
        If the group of tests has only one test, the test letter is omitted.
        Otherwise the test letters are lowercase english letters in alphabetical order, starting from 'a'.
        Examples of test names: "test1a", "test2", "codility1b", "codility1c", "recursion3", etc.
        Test names in the array are not sorted by their groups: i.e. ["test1a", "test2", "test1b", "test3", "test1c"]

        Test results are strings: "OK", "Wrong answer", "Time limit exceeded", "Runtime error".
        Only "OK" ones are considered as successful tests.

        Success rate is the number of passed groups of tests divided by the total number of groups.
        A group of tests is considered as passed if all tests in the group are passed.
        For example, with:
        tests = ["codility1", "codility3", "codility2", "codility4b", "codility4a"], and
        results = ["Wrong answer", "OK", "OK", "Runtime error", "OK"], then
        the success rate is 50, because there are 4 groups of tests, and only groups 2 and 3 have passed all the tests.
        """
        grouped_results = {}
        for i in range(len(tests)):
            group_no = re.search(r'\d+', tests[i]).group()
            if group_no not in grouped_results:
                grouped_results[group_no] = []
            grouped_results[group_no].append(results[i])
        total_groups = len(grouped_results)
        passed_groups = 0
        for key, value in grouped_results.items():
            group_failed = False
            for res in value:
                if res != "OK":
                    group_failed = True
                    break
            if not group_failed:
                passed_groups += 1
        return int(passed_groups / total_groups * 100)
