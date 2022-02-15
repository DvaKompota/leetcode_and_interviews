# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?

# Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34 ...


class BasicRecursion:

    def iterative_fibonacci(self, number: int):
        if number < 1:
            return "Invalid index in fibonacci sequence"
        if number == 1 or number == 2:
            return 1
        fibo1 = fibo2 = 1
        for i in range(3, number+1):
            fibo = fibo1 + fibo2
            fibo1, fibo2 = fibo2, fibo
        return fibo
    # RUNTIME: 0(n)
    # MEMORY: 0(1)

    def recursive_fibonacci(self, number: int):
        if number < 1:
            return "Invalid index in fibonacci sequence"
        if number == 1 or number == 2:
            return 1
        return self.recursive_fibonacci(number - 1) + self.recursive_fibonacci(number - 2)
    # RUNTIME: 0(2^n)
    # MEMORY: 0(n)

    def memoization_fibonacci(self, number: int, memo=None):
        if number < 1:
            return "Invalid index in fibonacci sequence"
        memo = {1: 1, 2: 1} if not memo else memo
        if number not in memo:
            memo[number] = self.memoization_fibonacci(number - 1, memo) + self.memoization_fibonacci(number - 2, memo)
        return memo[number]
    # RUNTIME: 0(n)
    # MEMORY: 0(n)

    def factorial(self, number: int):
        if number < 1:
            return "Invalid input for factorial"
        if number == 1:
            return 1
        return number * self.factorial(number - 1)
    # RUNTIME: 0(n)
    # MEMORY: 0(n)

    def sum_of_digits(self, number: int):
        if number < 1:
            return "Invalid input for adding digits"
        if number < 10:
            return number
        reminder = number % 10
        return reminder + self.sum_of_digits(int(number/10))
    # RUNTIME: O(lg(n))
    # MEMORY: O(lg(n))
