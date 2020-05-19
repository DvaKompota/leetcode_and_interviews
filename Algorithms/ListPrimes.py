# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?
#
# Count Primes
# Write a function that takes 'n' and finds all prime numbers that are smaller than this 'n'
# Example:
# Input: 10
# Output: [2, 3, 5, 7]
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class ListPrimes:
    def listPrimes(self, n: int) -> [int]:
        truth_table = n * [True]
        for i in range(2, int(n ** 0.5) + 1):
            for j in range(i * i, n, i):
                truth_table[j] = False

        primes = []
        for i in range(2, n):
            if truth_table[i]:
                primes.append(i)
        return primes
        # primes = [i for i in range(2, n) if truth_table[i]]
