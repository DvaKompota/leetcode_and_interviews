import unittest
from Tasks.InterviewTasks.NumbersToWordsConversion import NumbersToWordsConversion


class NumbersToWordsConversionTest(unittest.TestCase):

    def testNumbersToWordsConversion(self):
        given_string = '$121.09'
        expected_result = 'one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionPluralDollars(self):
        given_string = '$122.09'
        expected_result = 'one hundred twenty two dollars and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionSingleCent(self):
        given_string = '$121.31'
        expected_result = 'one hundred twenty one dollar and thirty one cent'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionZeroHundreds(self):
        given_string = '$21.09'
        expected_result = 'twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionZeroTens(self):
        given_string = '$101.09'
        expected_result = 'one hundred one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionThousand(self):
        given_string = '$1121.09'
        expected_result = 'one thousand one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionTenThousand(self):
        given_string = '$10121.09'
        expected_result = 'ten thousand one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionTwelveThousand(self):
        given_string = '$12121.09'
        expected_result = 'twelve thousand one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionHundredThousand(self):
        given_string = '$100121.09'
        expected_result = 'one hundred thousand one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionMillion(self):
        given_string = '$1000121.09'
        expected_result = 'one million one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionMillionAndThousand(self):
        given_string = '$1001121.09'
        expected_result = 'one million one thousand one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionMillionAndTenThousand(self):
        given_string = '$1010121.09'
        expected_result = 'one million ten thousand one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionMillionAndTwelveThousand(self):
        given_string = '$1012121.09'
        expected_result = 'one million twelve thousand one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionMillionAndHundredThousand(self):
        given_string = '$1100121.09'
        expected_result = 'one million one hundred thousand one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionTenMillion(self):
        given_string = '$10000121.09'
        expected_result = 'ten million one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionTwelveMillion(self):
        given_string = '$12000121.09'
        expected_result = 'twelve million one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionHundredMillion(self):
        given_string = '$100000121.09'
        expected_result = 'one hundred million one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionBillion(self):
        given_string = '$1000000121.09'
        expected_result = 'one billion one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)

    def testNumbersToWordsConversionTrillion(self):
        given_string = '$1000000000121.09'
        expected_result = 'one trillion one hundred twenty one dollar and nine cents'
        actual_result = NumbersToWordsConversion().numbers_to_words_conversion(given_string)
        self.assertEqual(expected_result, actual_result)
