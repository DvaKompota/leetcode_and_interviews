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


class FizzBuzz:

    def fizzBuzz(self, n: int) -> [str]:
        if n <= 0:
            return 'Invalid input'
        output = []
        for num in range(1, n+1):
            if num % 15 == 0:
                output.append('FizzBuzz')
            elif num % 5 == 0:
                output.append('Buzz')
            elif num % 3 == 0:
                output.append('Fizz')
            else:
                output.append(str(num))
        return output
