class CodilityTasks:

    # demo task
    """
    Given an array A of N integers, return the smallest positive integer (greater than 0) that does not occur in A.

    For example:
        Given A = [1, 3, 6, 4, 1, 2], the function should return 5.
        Given A = [1, 2, 3], the function should return 4.
        Given A = [−1, −3], the function should return 1.

    Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
    """
    def first_missing_integer(self, nums: [int, ]):
        nums_set = set()
        for num in nums:
            if num < 1:
                continue
            nums_set.add(num)
        for i in range(1, 1_000_000):
            if i not in nums_set:
                return i

    # Tesla Online Coding Assessment – https://app.codility.com/c/intro/3VTCJH-WKS/

    # task1
    def integer_matching_occurrences(self, arr: [int, ]):
        """
        Write a function that, given an array A consisting of N integers, returns the biggest value X,
        which occurs in A exactly X times.
        If there is no such value, the function should return 0.

        Examples:
            1. Given A = [3, 8, 2, 3, 3, 2], the function should return 3.
                The value 2 occurs exactly two times and the value 3 occurs exactly three times,
                so they both meet the task conditions.
                The value 8 occurs just once, thus it does not meet the task conditions.
                The maximum of 2 and 3 is 3.
            2. Given A = [7, 1, 2, 8, 2], the function should return 2.
                The value 1 occurs exactly one time; the value 2 occurs exactly two times.
            3. Given A = [3, 1, 4, 1, 5], the function should return 0.
                There is no value which meets the task conditions.
            4. Given A = [5, 5, 5, 5, 5], the function should return 5.

        Write an efficient algorithm for the following assumptions:
            - N is an integer within the range [1..100,000];
            - each element of array A is an integer within the range [1..1,000,000,000].
        """
        numbers_dict = {}
        for number in arr:
            if number not in numbers_dict:
                numbers_dict[number] = 1
            else:
                numbers_dict[number] += 1
        biggest_number = 0
        for key, value in numbers_dict.items():
            if key == value and value > biggest_number:
                biggest_number = value
        return biggest_number

    # task2
    def replace_question_marks(self, riddle: str):
        """
        Rick is a fan of logic-based games.
        However, he is bored of the classic ones, like Sudoku and Mastermind, since he has solved so many of them.
        Recently he found a new game in which one is given a string with some question marks in it.
        The objective is to replace all of the question marks with letters (one letter per question mark) in such a way
        that no letter appears next to another letter of the same kind.

        Write a function that, given a string, returns a copy of the string with all of the question marks replaced by
        lowercase letters (a−z) in such a way that the same letters do not occur next to each other.
        The result can be any of the possible answers as long as it fulfils the above requirements.

        Examples:
            1. Given riddle = "ab?ac?", your function might return "abcaca". Some other possible results are "abzacd", "abfacf".
            2. Given riddle = "rd?e?wg??", your function might return "rdveawgab".
            3. Given riddle = "????????", your function might return "codility".

        Write an efficient algorithm for the following assumptions:
            - the length of the string is within the range [1..100,000];
            - string riddle consists only of lowercases letters (a – z) or '?';
            - it is always possible to turn the input string into a string without two identical consecutive letters.
        """
        answer = ""
        replacements = ["a", "b", "c"]
        for index, char in enumerate(riddle):
            if char != "?":
                answer += char
            else:
                prev_char = answer[-1] if index != 0 else ""
                next_char = riddle[index + 1] if index != len(riddle) - 1 else ""
                for letter in replacements:
                    if letter not in [prev_char, next_char]:
                        answer += letter
                        break
        return answer

    # task3 was a quiz with 10 questions on Selenium

    # task4
    def square_from_wooden_sticks(self, first_stick: int, second_stick: int):
        """
        There are two wooden sticks of lengths A and B respectively.
        Each of them can be cut into shorter sticks of integer lengths.
        Our goal is to construct the largest possible square.
        In order to do this, we want to cut the sticks in such a way as to achieve four sticks of the same length
        (note that there can be some leftover pieces). What is the longest side of square that we can achieve?

        Input: two integers A, B
        Output: an integer of length of the largest square side that we can have, if not possible return 0.

        Examples:
            1. Given A = 10, B = 21, the function should return 7.
                We can cut the second stick into three sticks of length 7 and shorten the first stick by 3.
            2. Given A = 13, B = 11, the function should return 5.
                We can cut two sticks of length 5 from each of the given sticks.
            3. Given A = 2, B = 1, the function should return 0.
                It is not possible to make any square from the given sticks.
            4. Given A = 1, B = 8, the function should return 2.
                We can cut stick B into four parts.

        Write an efficient algorithm for the following assumptions:
        A and B are integers within the range [1..1,000,000,000].
        """
        answer = 0
        answer = max(answer, first_stick // 4)
        answer = max(answer, second_stick // 4)
        if first_stick >= second_stick // 3:
            answer = max(answer, second_stick // 3)
        if first_stick >= (second_stick // 2) * 2:
            answer = max(answer, second_stick // 2)
        if second_stick >= (first_stick // 2) * 2:
            answer = max(answer, first_stick // 2)
        if second_stick >= first_stick // 3:
            answer = max(answer, first_stick // 3)
        return answer
