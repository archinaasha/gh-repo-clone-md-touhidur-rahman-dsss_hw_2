import unittest

from math_quiz.math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min = 1
        max = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min, max)
            self.assertTrue(min <= rand_num <= max)

    def test_function_B(self):
        # TODO
        result = function_B()
        self.assertIn(result, ['+', '-', '*'])
        pass

    def test_function_C(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 2, '-', "10 - 2", 8),
            (5, 5, '*', "5 * 5", 25)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
                question, answer = function_C(num1, num2, operator)
                self.assertEqual(question, expected_problem)
                self.assertEqual(answer, expected_answer)
        pass

if __name__ == "__main__":
    unittest.main()
