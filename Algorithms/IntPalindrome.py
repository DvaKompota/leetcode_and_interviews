class IntPalindromeFirstDraft:

    def digit_length(self, number):
        counter = 1
        while number >= 10**counter:
            counter += 1
        return counter

    def is_palindrome(self, number=None):
        if number is None or number < 0:
            return False
        length = self.digit_length(number)
        for i in range(1, length, 2):
            first_digit = number//10 ** (length - i)
            number = int(number - first_digit*10 ** (length - i))
            last_digit = number % 10
            number = int(number/10)
            if first_digit != last_digit:
                return False
        return True


class IntPalindrome:

    def is_palindrome(self, number=None):
        if number is None or number < 0:
            return False
        incoming_number = number
        reversed_number = 0
        while number > 0:
            last_digit = number % 10
            reversed_number = reversed_number*10 + last_digit
            number = int(number/10)
        return reversed_number == incoming_number
