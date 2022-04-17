#   Write a function that takes in a non-empty string and that returns a boolean
#   representing whether the string is a palindrome.
#
#   A palindrome is defined as a string that's written the same forward and
#   backward. Note that single-character strings are palindromes.
#
#   Sample Input:
#   string = "abcdcba"
#
#   Sample Output:
#   True


def is_palindrome(string):
    reversed_string = ""
    for letter in string[::-1]:
        reversed_string += letter
    return reversed_string == string
