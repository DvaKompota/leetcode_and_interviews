import unittest
from Tasks.AlgoExpertTasks.BubbleSort import bubble_sort


class BubbleSortTest(unittest.TestCase):

    def testBubbleSort(self):
        array = [8, 5, 2, 9, 5, 6, 3]
        expected_result = [2, 3, 5, 5, 6, 8, 9]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSort1(self):
        array = [1]
        expected_result = [1]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSort12(self):
        array = [1, 2]
        expected_result = [1, 2]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSort21(self):
        array = [2, 1]
        expected_result = [1, 2]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSort132(self):
        array = [1, 3, 2]
        expected_result = [1, 2, 3]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSort312(self):
        array = [3, 1, 2]
        expected_result = [1, 2, 3]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSort123(self):
        array = [1, 2, 3]
        expected_result = [1, 2, 3]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSortLong(self):
        array = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]
        expected_result = [-10, -7, -7, -6, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 8, 10]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSortLong2(self):
        array = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]
        expected_result = [-10, -10, -9, -7, -7, -6, -5, -2, 2, 2, 3, 3, 4, 5, 8, 8, 9, 10]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSortLong3(self):
        array = [8, -6, 7, 10, 8, -1, 6, 2, 4, -5, 1, 10, 8, -10, -9, -10, 8, 9, -2, 7, -2, 4]
        expected_result = [-10, -10, -9, -6, -5, -2, -2, -1, 1, 2, 4, 4, 6, 7, 7, 8, 8, 8, 8, 9, 10, 10]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSortLong4(self):
        array = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
        expected_result = [-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSortLong5(self):
        array = [2, -2, -10, 10, 4, -8, -1, -8, -4, 7, -4, 0, 9, -9, 0, -9, -9, 4, 8, 5, 1, 5, 0, 0, 2, -10]
        expected_result = [-10, -10, -9, -9, -9, -8, -8, -4, -4, -2, -1, 0, 0, 0, 0, 1, 2, 2, 4, 4, 5, 5, 7, 8, 9, 10]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSortVeryLong(self):
        array = [427, 787, 222, 996, -359, -614, 246, 230, 107, -706, 568, 9, -246, 12, -764, -212, -484, 603, 934,
                 -848, -646, -991, 661, -32, -348, -474, -439, -56, 507, 736, 635, -171, -215, 564, -710, 710, 565,
                 892, 970, -755, 55, 821, -3, -153, 240, -160, -610, -583, -27, 131]
        expected_result = [-991, -848, -764, -755, -710, -706, -646, -614, -610, -583, -484, -474, -439, -359, -348,
                           -246, -215, -212, -171, -160, -153, -56, -32, -27, -3, 9, 12, 55, 107, 131, 222, 230, 240,
                           246, 427, 507, 564, 565, 568, 603, 635, 661, 710, 736, 787, 821, 892, 934, 970, 996]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)

    def testBubbleSortVeryLong2(self):
        array = [-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415,
                 -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730,
                 -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243,
                 610, -36, -685, -337, -13, 295, 800, -950, -949, -257, 631, -542, 201, -796, 157, 950, 540, -846,
                 -265, 746, 355, -578, -441, -254, -941, -738, -469, -167, -420, -126, -410, 59]
        expected_result = [-987, -950, -949, -942, -941, -935, -908, -874, -855, -846, -823, -817, -796, -738, -733,
                           -730, -685, -578, -575, -575, -544, -542, -469, -441, -420, -415, -410, -376, -371, -363,
                           -359, -353, -337, -293, -265, -257, -254, -191, -167, -160, -155, -126, -120, -51, -36, -13,
                           14, 48, 52, 59, 59, 125, 157, 164, 183, 201, 238, 243, 295, 323, 328, 341, 355, 356, 372,
                           399, 422, 490, 490, 540, 572, 610, 631, 646, 700, 724, 746, 800, 829, 842, 888, 892, 892,
                           919, 950, 965, 980, 995]
        actual_result = bubble_sort(array)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
