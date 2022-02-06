# 1. Input: What is the input parameter?
# 2. Output: What is the datatype of your answer that your function has to return?
# 3. What data structures and methods associated with it will be used
# 4. Where are you going to store temp data ( if needed )
# 5. Describe the model of your algorithm before implementing solution in code
# 6. Write unit tests for your solution -- think about edge cases
# 7. Runtime Complexity?
# 8. Memory Complexity?
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
# ["flower","flow","flight"] -> "fl"
#
# Example 2:
# ["dog","racecar","car"] -> ""
#
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.


from typing import List


class LongestCommonPrefix:

    def longest_common_prefix(self, strs: List[str]):
        common_prefix = ""
        shortest_word = strs[0]
        min_length = len(shortest_word)
        for word in strs:
            if len(word) < min_length:
                shortest_word = word
                min_length = len(shortest_word)
        for i in range(min_length):
            for word in strs:
                if word[i] != shortest_word[i]:
                    return common_prefix
            common_prefix += shortest_word[i]
        return common_prefix

# RUNTIME: 0(S) where S is the sum of all characters in all strings, which is 200*200
# MEMORY: 0(1)
