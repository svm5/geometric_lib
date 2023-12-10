import unittest

import square


class SquareTestCase(unittest.TestCase):
    delta = 0.001

    def test_arguments_instance(self):
        tests_count = 5
        input_data = ['1', [555], "fjkls", set([1, 2, 1, 3]), "12.5"]
 
        # for area()
        for i in range(tests_count):
            a = input_data[i]
            with self.assertRaises(ValueError):
                square.area(a)

        # for perimeter()
        for i in range(tests_count):
            a = input_data[i]
            with self.assertRaises(ValueError):
                square.perimeter(a)
    
    def test_side_length(self):
        tests_count = 3
        input_data = [-10, -38.8, -312891284]

        # for area()
        for i in range(tests_count):
            a = input_data[i]
            with self.assertRaises(ValueError):
                square.area(a)

        # for perimeter()
        for i in range(tests_count):
            a = input_data[i]    
            with self.assertRaises(ValueError):
                square.perimeter(a)

    def test_zero(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.perimeter(0), 0)

    def test_area(self):
        tests_count = 5
        input_data = [1, 10, 2.5, 5642, 589.67]
        expected_results = [1, 100, 6.25, 31832164, 347710.709]

        for i in range(tests_count):
            a = input_data[i]
            result_area = square.area(a)
            expected_area = expected_results[i]

            self.assertAlmostEqual(result_area, expected_area, delta=self.delta)
        
    def test_perimeter(self):
        tests_count = 5
        input_data = [1, 10, 2.5, 5642, 589.67]
        expected_results = [4, 40, 10, 22568, 2358.68]

        for i in range(tests_count):
            a = input_data[i]
            result_perimeter = square.perimeter(a)
            expected_perimeter = expected_results[i]

            self.assertAlmostEqual(result_perimeter, expected_perimeter, delta=self.delta)

    def test_result_instance(self):
        tests_count = 3
        input_data_int = [2, 50, 409842354]
        input_data_float = [5.2, 77.1, 409842354.67]
        
        for i in range(tests_count):
            a = input_data_int[i]

            self.assertIsInstance(square.area(a), int)
            self.assertIsInstance(square.perimeter(a), int)

        for i in range(tests_count):
            a = input_data_float[i]

            self.assertIsInstance(square.area(a), float)
            self.assertIsInstance(square.perimeter(a), float)