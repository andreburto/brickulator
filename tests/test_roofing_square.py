# Standard library
import os, unittest, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Local
from brickulator.roofing import square


# TODO: There are a lot of patterns in these tests. Refactor to use them and make the test DRY.
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

    def test_slope_bricks_per_level_per_side1(self):
        level_width = 8
        expected_results = (2, 0, 0)
        actual_results = square.slope_bricks_per_level_per_side(level_width)
        self.assertTupleEqual(expected_results, actual_results)

    def test_slope_bricks_per_level_per_side2(self):
        level_width = 18
        expected_results = (4, 1, 0)
        actual_results = square.slope_bricks_per_level_per_side(level_width)
        self.assertTupleEqual(expected_results, actual_results)

    def test_slope_bricks_per_level_per_side3(self):
        level_width = 19
        expected_results = (4, 1, 1)
        actual_results = square.slope_bricks_per_level_per_side(level_width)
        self.assertTupleEqual(expected_results, actual_results)

    def test_slope_bricks_per_level1(self):
        side_widths = [4, 4, 4, 4]
        expected_results = (4, 0, 0, 0)
        actual_results = square.slope_bricks_per_level(side_widths)
        self.assertTupleEqual(expected_results, actual_results)

    def test_slope_bricks_per_level2(self):
        side_widths = [10, 10, 10, 10]
        expected_results = (4, 4, 4, 0)
        actual_results = square.slope_bricks_per_level(side_widths)
        self.assertTupleEqual(expected_results, actual_results)

    def test_bricks_per_square_roof(self):
        base_width = 8
        expected_results = (12, 4, 4, 0)
        actual_results = square.bricks_per_square_roof(base_width)
        self.assertTupleEqual(expected_results, actual_results)

    def test_bricks_per_square_roof(self):
        base_width = 11
        expected_results = (16, 8, 8, 16)
        actual_results = square.bricks_per_square_roof(base_width)
        self.assertTupleEqual(expected_results, actual_results)
