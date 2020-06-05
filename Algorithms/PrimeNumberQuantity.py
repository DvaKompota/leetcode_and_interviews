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
# Count the number of prime numbers less than a non-negative number, n.
# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class PrimeNumberQuantityBruteForce:

    def prime_number_quantity(self, n: int) -> int:
        answer = 0
        for number in range(1, n):
            counter = 0
            for divider in range(1, number+1):
                if number % divider == 0 and divider != 1:
                    counter += 1
            if counter == 1:
                answer += 1
        return answer


class PrimeNumberQuantity:

    def prime_number_quantity(self, n: int) -> int:
        answer = 0
        arr = []
        for i in range(0, n):
            arr.append(True)

        i = 2
        while i * i < n:
            if arr[i] is True:
                j = 2
                while j * i < n:
                    arr[j*i] = False
                    j += 1
            i += 1

        for item in arr[2:]:
            if item == True:
                answer += 1
        return answer
