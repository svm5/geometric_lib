import unittest

import triangle


class TriangleTestCase(unittest.TestCase):
    delta = 0.001

    def test_area_arguments_instance(self):
        tests_count = 5
        input_data = [('1', 1), ([555], 8), ("fjkls", [1, 2, 3]), (123, set([1, 2, 1, 3])), ("12.5", 65.7)]
 
        for i in range(tests_count):
            a, h = input_data[i]
            with self.assertRaises(ValueError):
                triangle.area(a, h)

    def test_perimeter_arguments_instance(self):
        tests_count = 5
        input_data = [('1', 2, '5'),
                      ([555], 8, [1, 2, 3]),
                      ("fjkls", "fdg", list()),
                      (123, set([1, 2, 1, 3]), {}),
                      ("12.5", 65.7, [1.23])]
 
        for i in range(tests_count):
            a, b, c = input_data[i]
            with self.assertRaises(ValueError):
                triangle.perimeter(a, b, c)
    
    def test_sides_length_area(self):
        tests_count = 3
        area_input_data = [(-10, 20), (-10, -10.89), (30.7, -100)]

        for i in range(tests_count):
            a, h = area_input_data[i]
            with self.assertRaises(ValueError):
                triangle.area(a, h)

    def test_sides_length_perimeter(self):
        tests_count = 3
        perimeter_input_data = [(-10, 20, 59), (-10, -10.89, -8.6), (-83.8, 30.7, -100)]
        # for perimeter()
        for i in range(tests_count):
            a, b, c = perimeter_input_data[i]    
            with self.assertRaises(ValueError):
                triangle.perimeter(a, b, c)

    def test_zero_area(self):
        tests_count = 5
        input_data = [(10, 0), (12345, 0), (0, 95), (0, 736.48), (0, 0)]
        area_expected_results = [0, 0, 0, 0, 0, 0]
        
        for i in range(tests_count):
            a, h = input_data[i]
            result_area = triangle.area(a, h)
            expected_area = area_expected_results[i]

            self.assertEqual(result_area, expected_area)

    def test_zero_perimeter(self):
        tests_count = 5
        input_data = [(10, 0, 0), (0, 12345, 0), (0, 0, 9.5), (0, 736.48, 0), (0, 0, 0)]
        perimeter_expected_results = [10, 12345, 9.5, 736.48, 0]
        
        for i in range(tests_count):
            a, b, c = input_data[i]
            result_perimeter = triangle.perimeter(a, b, c)
            expected_perimeter = perimeter_expected_results[i]

            self.assertEqual(result_perimeter, expected_perimeter)
        
    def test_area(self):
        tests_count = 5
        input_data = [(10, 2), (2.3, 4), (1, 8.5), (31, 633), (12.3, 62.5)]
        area_expected_results = [10, 4.6, 4.25, 9811.5, 384.375]

        for i in range(tests_count):
            a, h = input_data[i]
            result_area = triangle.area(a, h)
            expected_area = area_expected_results[i]

            self.assertAlmostEqual(result_area, expected_area, delta=self.delta)
        
    def test_perimeter(self):
        tests_count = 5
        input_data = [(10, 2, 20), (2.3, 4, 7.5), (1, 8.5, 801), (5830, 31, 633), (31.67, 12.3, 62.5)]
        perimeter_expected_results = [32, 13.8, 810.5, 6494, 106.47]

        for i in range(tests_count):
            a, b, c = input_data[i]
            result_perimeter = triangle.perimeter(a, b, c)
            expected_perimeter = perimeter_expected_results[i]

            self.assertAlmostEqual(result_perimeter, expected_perimeter, delta=self.delta)

    def test_commutativity_perimeter(self):
        tests_count = 5
        input_data = [(5, 5, 10), (2, 8, 23), (3.7, 6, 86.8), (11, 71.7, 2), (39.6, 29.9, 83.7)]

        for i in range(tests_count):
            a, b, c = input_data[i]

            self.assertAlmostEqual(triangle.perimeter(a, b, c), triangle.perimeter(a, c, b), delta=self.delta)
            self.assertAlmostEqual(triangle.perimeter(a, c, b), triangle.perimeter(b, a, c), delta=self.delta)
            self.assertAlmostEqual(triangle.perimeter(b, a, c), triangle.perimeter(b, c, a), delta=self.delta)
            self.assertAlmostEqual(triangle.perimeter(b, c, a), triangle.perimeter(c, a, b), delta=self.delta)
            self.assertAlmostEqual(triangle.perimeter(c, a, b), triangle.perimeter(c, b, a), delta=self.delta)

    def test_area_result_instance(self):
        tests_count = 6
        input_data = [(2, 8), (50, 77), (47289, 409842354), 
                      (5.2, 8.6), (50.6, 77.1), (47289.234, 409842354.67)]
        
        for i in range(tests_count):
            a, h = input_data[i]

            self.assertIsInstance(triangle.area(a, h), float)

    def test_perimeter_result_instance(self):
        tests_count = 3
        input_data_int = [(2, 8, 45), (50, 77, 8902), (47289, 409842354, 28395235)]
        input_data_float = [(5, 5.2, 8.6), (50.6, 77, 4230), (47289.234, 40954.67, 1.1)]
        
        for i in range(tests_count):
            a, b, c = input_data_int[i]

            self.assertIsInstance(triangle.perimeter(a, b, c), int)

        for i in range(tests_count):
            a, b, c = input_data_float[i]

            self.assertIsInstance(triangle.perimeter(a, b, c), float)