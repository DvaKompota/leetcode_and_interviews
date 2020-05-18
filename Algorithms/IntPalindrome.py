class IntPalindromeFirstDraft:

    def is_palindrome(self, number=None):
        if number is None or number < 0:
            return False
        length = 1
        while number >= 10 ** length:
            length += 1
        for i in range(1, length, 2):
            first_digit = number//10 ** (length - i)
            number = int(number - first_digit*10 ** (length - i))
            last_digit = number % 10
            number = int(number/10)
            if first_digit != last_digit:
                return False
        return True


class IntPalindrome:

    def isPalindrome(self, x: int) -> bool:
        if x is None or x < 0:
            return False
        incoming_x = x
        reversed_x = 0
        while x > 0:
            last_digit = x % 10
            reversed_x = reversed_x*10 + last_digit
            x = int(x/10)
        return reversed_x == incoming_x
