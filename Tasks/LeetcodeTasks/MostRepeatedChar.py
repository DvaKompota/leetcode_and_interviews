# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?

# Given a string find the most repeated character in that string

class MostRepeatedChar:

    def most_repeated_char(self, str1: str):
        chars = {}
        for letter in str1:
            if letter not in chars.keys():
                chars.update({letter: 1})
            else:
                chars[letter] += 1
        max_value = 0
        for k, v in chars.items():
            if v > max_value:
                max_value = v
                char = k
        return char

    # RUNTIME: 0(n)
    # MEMORY: 0(n)
