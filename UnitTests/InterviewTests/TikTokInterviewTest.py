import unittest
from Tasks.InterviewTasks.TikTokInterview import TikTokInterview


class TikTokInterviewFindMismatchTest(unittest.TestCase):

    def testTikTokInterviewFindMismatch1(self):
        arr1 = ['a', 'b', 'c', 'd']
        arr2 = ['a', 'b', 'c', 'e']
        expected_result = 'e'
        actual_result = TikTokInterview().find_mismatch(arr1, arr2)
        self.assertEqual(expected_result, actual_result)

    def testTikTokInterviewFindMismatch2(self):
        arr1 = ['a', 'b', 'c', 'd']
        arr2 = ['b', 'a', 'c']
        expected_result = 'd'
        actual_result = TikTokInterview().find_mismatch(arr1, arr2)
        self.assertEqual(expected_result, actual_result)

    def testTikTokInterviewFindMismatch3(self):
        arr1 = ['a', 'b', 'c']
        arr2 = ['c', 'b', 'a', 'e']
        expected_result = 'e'
        actual_result = TikTokInterview().find_mismatch(arr1, arr2)
        self.assertEqual(expected_result, actual_result)

    def testTikTokInterviewFindMismatch4(self):
        arr1 = ['a', 'b', 'c']
        arr2 = ['a', 'b', 'c', 'c']
        expected_result = 'c'
        actual_result = TikTokInterview().find_mismatch(arr1, arr2)
        self.assertEqual(expected_result, actual_result)

    def testTikTokInterviewFindMismatch5(self):
        arr1 = ['a', 'b', 'c', 'c']
        arr2 = ['a', 'c', 'b']
        expected_result = 'c'
        actual_result = TikTokInterview().find_mismatch(arr1, arr2)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
