import unittest
from Algorithms.GoogleInterview import GoogleInterview


class GoogleInterviewProcessStringTest(unittest.TestCase):

    def testGoogleInterviewProcessStringProcessStringStartQuotes(self):
        given_string = '"Google",GOO21W,Pixel,629.10'
        expected_result = {'Company': 'Google',
                           'SKU': 'GOO21W',
                           'Description': 'Pixel',
                           'Price': '629.10'}
        actual_result = GoogleInterview().process_string(given_string)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewProcessStringMiddleQuotes(self):
        given_string = 'Google,GOO21W,"Pixel 5, 5G, Google-assistance",629.10'
        expected_result = {'Company': 'Google',
                           'SKU': 'GOO21W',
                           'Description': 'Pixel 5, 5G, Google-assistance',
                           'Price': '629.10'}
        actual_result = GoogleInterview().process_string(given_string)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewProcessStringEndQuotes(self):
        given_string = 'Google,GOO21W,Pixel,"629.10"'
        expected_result = {'Company': 'Google',
                           'SKU': 'GOO21W',
                           'Description': 'Pixel',
                           'Price': '629.10'}
        actual_result = GoogleInterview().process_string(given_string)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewProcessStringMultiQuotes(self):
        given_string = '"Google",GOO21W,"Pixel 5, 5G, Google-assistance",629.10'
        expected_result = {'Company': 'Google',
                           'SKU': 'GOO21W',
                           'Description': 'Pixel 5, 5G, Google-assistance',
                           'Price': '629.10'}
        actual_result = GoogleInterview().process_string(given_string)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewProcessStringStartEmpty(self):
        given_string = ',GOO21W,"Pixel 5, 5G, Google-assistance",629.10'
        expected_result = {'Company': '',
                           'SKU': 'GOO21W',
                           'Description': 'Pixel 5, 5G, Google-assistance',
                           'Price': '629.10'}
        actual_result = GoogleInterview().process_string(given_string)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewProcessStringMiddleEmpty(self):
        given_string = 'Google,,"Pixel 5, 5G, Google-assistance",629.10'
        expected_result = {'Company': 'Google',
                           'SKU': '',
                           'Description': 'Pixel 5, 5G, Google-assistance',
                           'Price': '629.10'}
        actual_result = GoogleInterview().process_string(given_string)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewProcessStringQuotesEmpty(self):
        given_string = 'Google,GOO21W,"",629.10'
        expected_result = {'Company': 'Google',
                           'SKU': 'GOO21W',
                           'Description': '',
                           'Price': '629.10'}
        actual_result = GoogleInterview().process_string(given_string)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewProcessStringEndEmpty(self):
        given_string = 'Google,GOO21W,"Pixel 5, 5G, Google-assistance",'
        expected_result = {'Company': 'Google',
                           'SKU': 'GOO21W',
                           'Description': 'Pixel 5, 5G, Google-assistance',
                           'Price': ''}
        actual_result = GoogleInterview().process_string(given_string)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewProcessStringMultiEmpty(self):
        given_string = 'Google,GOO21W,"",'
        expected_result = {'Company': 'Google',
                           'SKU': 'GOO21W',
                           'Description': '',
                           'Price': ''}
        actual_result = GoogleInterview().process_string(given_string)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewProcessStringAllEmpty(self):
        given_string = ',,"",'
        expected_result = {'Company': '',
                           'SKU': '',
                           'Description': '',
                           'Price': ''}
        actual_result = GoogleInterview().process_string(given_string)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
