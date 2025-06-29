import unittest
from Tasks.AlgoExpertTasks.StaircaseTraversal import staircase_traversal_recursive_memoization, \
    staircase_traversal_iterative_nested_sum, staircase_traversal_iterative_remove_add


class StaircaseTraversalRecursiveMemoizationTest(unittest.TestCase):

    def testStaircaseTraversalRecursiveMemoization_1(self):
        height = 4
        max_steps = 2
        expected_result = 5
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_2(self):
        height = 10
        max_steps = 1
        expected_result = 1
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_3(self):
        height = 10
        max_steps = 2
        expected_result = 89
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_4(self):
        height = 4
        max_steps = 3
        expected_result = 7
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_5(self):
        height = 1
        max_steps = 1
        expected_result = 1
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_6(self):
        height = 5
        max_steps = 2
        expected_result = 8
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_7(self):
        height = 4
        max_steps = 4
        expected_result = 8
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_8(self):
        height = 6
        max_steps = 2
        expected_result = 13
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_9(self):
        height = 100
        max_steps = 1
        expected_result = 1
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_10(self):
        height = 15
        max_steps = 5
        expected_result = 13624
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_11(self):
        height = 7
        max_steps = 2
        expected_result = 21
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_12(self):
        height = 6
        max_steps = 3
        expected_result = 24
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalRecursiveMemoization_13(self):
        height = 3
        max_steps = 2
        expected_result = 3
        actual_result = staircase_traversal_recursive_memoization(height, max_steps)
        self.assertEqual(actual_result, expected_result)


class StaircaseTraversalIterativeNestedSumTest(unittest.TestCase):

    def testStaircaseTraversalIterativeNestedSum_1(self):
        height = 4
        max_steps = 2
        expected_result = 5
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_2(self):
        height = 10
        max_steps = 1
        expected_result = 1
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_3(self):
        height = 10
        max_steps = 2
        expected_result = 89
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_4(self):
        height = 4
        max_steps = 3
        expected_result = 7
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_5(self):
        height = 1
        max_steps = 1
        expected_result = 1
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_6(self):
        height = 5
        max_steps = 2
        expected_result = 8
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_7(self):
        height = 4
        max_steps = 4
        expected_result = 8
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_8(self):
        height = 6
        max_steps = 2
        expected_result = 13
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_9(self):
        height = 100
        max_steps = 1
        expected_result = 1
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_10(self):
        height = 15
        max_steps = 5
        expected_result = 13624
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_11(self):
        height = 7
        max_steps = 2
        expected_result = 21
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_12(self):
        height = 6
        max_steps = 3
        expected_result = 24
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeNestedSum_13(self):
        height = 3
        max_steps = 2
        expected_result = 3
        actual_result = staircase_traversal_iterative_nested_sum(height, max_steps)
        self.assertEqual(actual_result, expected_result)


class StaircaseTraversalIterativeRemoveAddTest(unittest.TestCase):

    def testStaircaseTraversalIterativeRemoveAdd_1(self):
        height = 4
        max_steps = 2
        expected_result = 5
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_2(self):
        height = 10
        max_steps = 1
        expected_result = 1
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_3(self):
        height = 10
        max_steps = 2
        expected_result = 89
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_4(self):
        height = 4
        max_steps = 3
        expected_result = 7
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_5(self):
        height = 1
        max_steps = 1
        expected_result = 1
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_6(self):
        height = 5
        max_steps = 2
        expected_result = 8
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_7(self):
        height = 4
        max_steps = 4
        expected_result = 8
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_8(self):
        height = 6
        max_steps = 2
        expected_result = 13
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_9(self):
        height = 100
        max_steps = 1
        expected_result = 1
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_10(self):
        height = 15
        max_steps = 5
        expected_result = 13624
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_11(self):
        height = 7
        max_steps = 2
        expected_result = 21
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_12(self):
        height = 6
        max_steps = 3
        expected_result = 24
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)

    def testStaircaseTraversalIterativeRemoveAdd_13(self):
        height = 3
        max_steps = 2
        expected_result = 3
        actual_result = staircase_traversal_iterative_remove_add(height, max_steps)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
