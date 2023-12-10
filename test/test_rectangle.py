import unittest

import rectangle


class RectangleTestCase(unittest.TestCase):
    delta = 0.001

    def test_arguments_instance(self):
        tests_count = 5
        input_data = [('1', 1), ([555], 8), ("fjkls", [1, 2, 3]), (123, set([1, 2, 1, 3])), ("12.5", 65.7)]
 
        # for area()
        for i in range(tests_count):
            a, b = input_data[i]
            with self.assertRaises(ValueError):
                rectangle.area(a, b)

        # for perimeter()
        for i in range(tests_count):
            a, b = input_data[i]
            with self.assertRaises(ValueError):
                rectangle.perimeter(a, b)
    
    def test_sides_length(self):
        tests_count = 3
        input_data = [(-10, 20), (-10, -100), (30, -100)]

        # for area()
        for i in range(tests_count):
            a, b = input_data[i]
            with self.assertRaises(ValueError):
                rectangle.area(a, b)

        # for perimeter()
        for i in range(tests_count):
            a, b = input_data[i]    
            with self.assertRaises(ValueError):
                rectangle.perimeter(a, b)

    def test_zero_area(self):
        tests_count = 5
        input_data = [(10, 0), (12345, 0), (0, 95), (0, 736.48), (0, 0)]
        area_expected_results = [0, 0, 0, 0, 0, 0]
        
        for i in range(tests_count):
            a, b = input_data[i]
            result_area = rectangle.area(a, b)
            expected_area = area_expected_results[i]

            self.assertEqual(result_area, expected_area)

    def test_zero_perimeter(self):
        tests_count = 5
        input_data = [(10, 0), (12345, 0), (0, 95), (0, 736.48), (0, 0)]
        perimeter_expected_results = [20, 24690, 190, 1472.96, 0]
        
        for i in range(tests_count):
            a, b = input_data[i]
            result_perimeter = rectangle.perimeter(a, b)
            expected_perimeter = perimeter_expected_results[i]

            self.assertEqual(result_perimeter, expected_perimeter)
       
    def test_square_area(self):
        tests_count = 5
        input_data = [(10, 10), (1, 1), (33, 33), (2.5, 2.5), (3.7, 3.7)]
        area_expected_results = [100, 1, 1089, 6.25, 13.69]

        for i in range(tests_count):
            a, b = input_data[i]
            result_area = rectangle.area(a, b)
            expected_area = area_expected_results[i]

            self.assertAlmostEqual(result_area, expected_area, delta=self.delta)

    def test_square_perimeter(self):
        tests_count = 5
        input_data = [(10, 10), (1, 1), (33, 33), (2.5, 2.5), (3.7, 3.7)]
        perimeter_expected_results = [40, 4, 132, 10, 14.8]

        for i in range(tests_count):
            a, b = input_data[i]
            result_perimeter = rectangle.perimeter(a, b)
            expected_perimeter = perimeter_expected_results[i]

            self.assertAlmostEqual(result_perimeter, expected_perimeter, delta=self.delta)
        
    def test_different_sides_area(self):
        tests_count = 5
        input_data = [(10, 2), (2.3, 4), (1, 8.5), (31, 633), (12.3, 62.5)]
        area_expected_results = [20, 9.2, 8.5, 19623, 768.75]

        for i in range(tests_count):
            a, b = input_data[i]
            result_area = rectangle.area(a, b)
            expected_area = area_expected_results[i]

            self.assertAlmostEqual(result_area, expected_area, delta=self.delta)
        
    def test_different_sides_perimeter(self):
        tests_count = 5
        input_data = [(10, 2), (2.3, 4), (1, 8.5), (31, 633), (12.3, 62.5)]
        perimeter_expected_results = [24, 12.6, 19, 1328, 149.6]

        for i in range(tests_count):
            a, b = input_data[i]
            result_perimeter = rectangle.perimeter(a, b)
            expected_perimeter = perimeter_expected_results[i]

            self.assertAlmostEqual(result_perimeter, expected_perimeter, delta=self.delta)

    def test_commutativity(self):
        tests_count = 5
        input_data = [(5, 5), (2, 8), (3.7, 6), (11, 71.7), (39.6, 29.9)]

        for i in range(tests_count):
            a, b = input_data[i]

            self.assertAlmostEqual(rectangle.area(a, b), rectangle.area(b, a), delta=self.delta)
            self.assertAlmostEqual(rectangle.perimeter(a, b), rectangle.perimeter(b, a), delta=self.delta)

    def test_result_instance(self):
        tests_count = 3
        input_data_int = [(2, 8), (50, 77), (47289, 409842354)]
        input_data_float = [(5.2, 8.6), (50.6, 77.1), (47289.234, 409842354.67)]
        
        for i in range(tests_count):
            a, b = input_data_int[i]

            self.assertIsInstance(rectangle.area(a, b), int)
            self.assertIsInstance(rectangle.perimeter(a, b), int)

        for i in range(tests_count):
            a, b = input_data_float[i]

            self.assertIsInstance(rectangle.area(a, b), float)
            self.assertIsInstance(rectangle.perimeter(a, b), float)