# Convert $121.09 to words. eg :
# one hundred twenty one dollars and nine cents.
# Make it as generic as possible to accept any number

import re


class NumbersToWordsConversion:

    def __init__(self):
        self.ones = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
                "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten",
                "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
                "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}
        self.tens = {"2": "twenty", "3": "thirty", "4": "fourty", "5": "fifty",
                "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}
        self.thousands = {"0": "", "1": " thousand ", "2": " million ", "3": " billion ", "4": " trillion "}

    def numbers_to_words_conversion(self, amount: [str]):
        phrase = ""

        dollars_and_cents = self.string_to_int_conversion(amount)

        if dollars_and_cents[0] > 999:
            dollars = self.split_dollars_in_thousands(dollars_and_cents[0])
        else:
            dollars = [dollars_and_cents[0]]
        dollars_phrase = ""
        for i, item in enumerate(dollars):
            dollars_phrase += self.int_to_words_conversion(item)
            if item != 0:
                dollars_phrase += self.thousands[str(len(dollars)-i-1)]

        cents = dollars_and_cents[-1]
        cents_phrase = self.int_to_words_conversion(cents)

        if dollars_phrase[-3:] != "one":
            phrase += dollars_phrase + " dollars"
        else:
            phrase += dollars_phrase + " dollar"
        phrase += " and "
        if cents_phrase[-3:] != "one":
            phrase += cents_phrase + " cents"
        else:
            phrase += cents_phrase + " cent"

        return phrase

    def split_dollars_in_thousands(self, amount: [int]):
        dollars_listed = []
        dollars_string = str(amount)
        while len(dollars_string) > 0:
            dollars_listed.insert(0, int(dollars_string[-3:]))
            dollars_string = dollars_string[:-3]
        return dollars_listed

    def string_to_int_conversion(self, amount: [str]):
        tmp = amount
        tmp = tmp.replace(" ", "")
        tmp = tmp.replace("'", "")
        tmp = tmp.replace("`'`", "")
        tmp = tmp.replace(",", "")
        tmp = re.findall('\\d+', tmp)
        dollars = int(tmp[0])
        cents = int(tmp[-1])
        return dollars, cents

    def int_to_words_conversion(self, amount: [int]):
        words = ""
        amount_str = str(amount)
        teen_flag = False

        if amount > 99:
            hundreds = self.ones[amount_str[0]]
            amount_str = amount_str[1:]
            if int(amount_str) != 0:
                words += hundreds + " hundred "
            else:
                words += hundreds + " hundred"

        if amount > 9:
            if amount_str[0] == "0":
                amount_str = amount_str[1:]
            elif amount_str[0] == "1":
                teen = self.ones[amount_str]
                words += teen
                teen_flag = True
            else:
                ten = self.tens[amount_str[0]]
                words += ten
                amount_str = amount_str[1:]
                if amount_str != "0":
                    words += " "

        if amount_str != "0" and teen_flag is False:
            one = self.ones[amount_str[0]]
            words += one

        return words
