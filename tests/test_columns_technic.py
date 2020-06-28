# Standard library
import os, unittest, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Local
from brickulator.columns import technic


class TestStringMethods(unittest.TestCase):

    def test_bricks_and_plates(self):
        # One plate == one plate
        self.assertTupleEqual((0, 1), technic.bricks_and_plates(1))
        # One brick == three plates
        self.assertTupleEqual((1, 0), technic.bricks_and_plates(3))
        # One brick, one plate == four plates
        self.assertTupleEqual((1, 1), technic.bricks_and_plates(4))

    def test_decrease_numbers(self):
        test_ratio_dict = technic.PLATE_TO_HOLE_MIN_DICT
        # Confirm that it won't decrease past the minimum.
        self.assertDictEqual(technic.PLATE_TO_HOLE_MIN_DICT, technic.decrease_numbers(test_ratio_dict))

    def test_increase_numbers(self):
        test_ratio_dict = technic.PLATE_TO_HOLE_MIN_DICT
        # One increase from the minimum
        increase_one = technic.increase_numbers(test_ratio_dict)
        self.assertDictEqual({'hole': 3, 'plate': 7}, increase_one)
        # Two increases from the minimum
        increase_two = technic.increase_numbers(increase_one)
        self.assertDictEqual({'hole': 5, 'plate': 12}, increase_two)
