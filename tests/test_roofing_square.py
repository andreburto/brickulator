# Standard library
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Local
from brickulator.roofing import square


class TestStringMethods(unittest.TestCase):

    def test_peg_width_per_levels1(self):
        base_width = 8
        expected_results = [8, 6, 4, 2]
        actual_results = square.peg_width_per_levels(base_width)
        self.assertListEqual(expected_results, actual_results)

    def test_peg_width_per_levels2(self):
        base_width = 10
        expected_results = [10, 8, 6, 4, 2]
        actual_results = square.peg_width_per_levels(base_width)
        self.assertListEqual(expected_results, actual_results)

    def test_peg_perimeter1(self):
        expected_perimeter = 12
        actual_perimeter = square.peg_perimeter([4, 4, 4, 4])
        self.assertEqual(expected_perimeter, actual_perimeter)

    def test_peg_perimeter2(self):
        expected_perimeter = 12
        actual_perimeter = square.peg_perimeter([4, 4, 4, 4])
        self.assertEqual(expected_perimeter, actual_perimeter)


    def test_corners_per_level1(self):
        expected_corners = 0
        actual_corners = square.corners_per_level([3, 3, 3, 3])
        self.assertEqual(expected_corners, actual_corners)


    def test_corners_per_level2(self):
        expected_corners = 4
        actual_corners = square.corners_per_level([4, 4, 4, 4])
        self.assertEqual(expected_corners, actual_corners)


    def test_corners_per_level3(self):
        expected_corners = 4
        actual_corners = square.corners_per_level([6, 6, 6, 6])
        self.assertEqual(expected_corners, actual_corners)
