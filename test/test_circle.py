import math
import unittest

import circle


class CircleTestCase(unittest.TestCase):
    delta = 0.001

    def test_arguments_instance(self):
        tests_count = 5
        input_data = ['1', [555], "fjkls", set([1, 2, 1, 3]), "12.5"]
 
        # for area()
        for i in range(tests_count):
            r = input_data[i]
            with self.assertRaises(ValueError):
                circle.area(r)

        # for perimeter()
        for i in range(tests_count):
            r = input_data[i]
            with self.assertRaises(ValueError):
                circle.perimeter(r)
    
    def test_radius_length(self):
        tests_count = 3
        input_data = [-10, -38.8, -312891284]

        # for area()
        for i in range(tests_count):
            r = input_data[i]
            with self.assertRaises(ValueError):
                circle.area(r)

        # for perimeter()
        for i in range(tests_count):
            r = input_data[i]    
            with self.assertRaises(ValueError):
                circle.perimeter(r)

    def test_zero(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)

    def test_area(self):
        tests_count = 5
        input_data = [1, 8, 2.5, 142, 125.6]
        expected_results = [math.pi * 1 * 1, 
                            math.pi * 8 * 8, 
                            math.pi * 2.5 * 2.5, 
                            math.pi * 142 * 142, 
                            math.pi * 125.6 * 125.6]

        for i in range(tests_count):
            r = input_data[i]
            result_area = circle.area(r)
            expected_area = expected_results[i]

            self.assertAlmostEqual(result_area, expected_area, delta=self.delta)
        
    def test_perimeter(self):
        tests_count = 5
        input_data = [1, 10, 2.5, 5642, 589.67]
        expected_results = [2 * math.pi * 1, 
                            2 * math.pi * 10, 
                            2 * math.pi * 2.5, 
                            2 * math.pi * 5642, 
                            2 * math.pi * 589.67]

        for i in range(tests_count):
            r = input_data[i]
            result_perimeter = circle.perimeter(r)
            expected_perimeter = expected_results[i]

            self.assertAlmostEqual(result_perimeter, expected_perimeter, delta=self.delta)

    def test_result_instance(self):
        tests_count = 3
        input_data_int = [2, 50, 409842354]
        input_data_float = [5.2, 77.1, 409842354.67]
        
        for i in range(tests_count):
            r = input_data_int[i]

            self.assertIsInstance(circle.area(r), float)
            self.assertIsInstance(circle.perimeter(r), float)

        for i in range(tests_count):
            r = input_data_float[i]

            self.assertIsInstance(circle.area(r), float)
            self.assertIsInstance(circle.perimeter(r), float)