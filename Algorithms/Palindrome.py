# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?

# Given a string return a boolean if the string is a palindrome or not


class Palindrome:

    def is_palindrome(self, str1: str):
        if str1 == "":
            return "The string is empty!"
        for i in range(int(len(str1)/2)):
            if str1[i] != str1[-(i+1)]:
                return False
        return True
    # RUNTIME: 0(n/2)
    # MEMORY: 0(1)
