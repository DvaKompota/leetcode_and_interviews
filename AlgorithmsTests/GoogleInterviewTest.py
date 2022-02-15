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


class GoogleInterviewCountDistanceTest(unittest.TestCase):

    def testGoogleInterviewCountDistance(self):
        start = "A"
        finish = "B"
        connections = [("A", "C"), ("B", "C"), ]
        expected_result = 2
        actual_result = GoogleInterview().count_distance(start, finish, connections)
        self.assertEqual(expected_result, actual_result)


class GoogleInterviewLuggageHandlingTest(unittest.TestCase):

    def testGoogleInterviewLuggageHandling(self):
        luggage_input = [10, 20, 15, 40, 25]
        expected_result = [25, 40, 15, 10, 20]
        actual_result = GoogleInterview().luggage_handling(luggage_input)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewLuggageHandlingOneContainer(self):
        luggage_input = [1, 2, 5, 4, 15]
        expected_result = [1, 2, 5, 4, 15]
        actual_result = GoogleInterview().luggage_handling(luggage_input)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewLuggageHandlingWithZero(self):
        luggage_input = [10, 0, 15, 40, 25]
        expected_result = [25, 40, 10, 0, 15]
        actual_result = GoogleInterview().luggage_handling(luggage_input)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewLuggageHandlingOneZero(self):
        luggage_input = [0]
        expected_result = [0]
        actual_result = GoogleInterview().luggage_handling(luggage_input)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewLuggageHandlingMultipleZeros(self):
        luggage_input = [0, 0, 0, 0]
        expected_result = [0, 0, 0, 0]
        actual_result = GoogleInterview().luggage_handling(luggage_input)
        self.assertEqual(expected_result, actual_result)

    def testGoogleInterviewLuggageHandlingTooBig(self):
        luggage_input = [1, 2, 5, 4, 41]
        with self.assertRaises(ValueError) as error:
            GoogleInterview().luggage_handling(luggage_input)
        self.assertEqual(str(error.exception), 'This is too big')

    def testGoogleInterviewLuggageHandlingEmpty(self):
        luggage_input = []
        with self.assertRaises(ValueError) as error:
            GoogleInterview().luggage_handling(luggage_input)
        self.assertEqual(str(error.exception), 'Nothing to transport')


class GoogleInterviewReplaceVarsInStringTest(unittest.TestCase):

    def testGoogleInterviewReplaceVarsInString(self):
        input_string = "/user/%USER%/home/%TMP%"
        vars_dict = {"USER": "foo",	"TMP": "tmp"}
        expected_result = "/user/foo/home/tmp"
        actual_result = GoogleInterview().replace_vars_in_string(input_string, vars_dict)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
