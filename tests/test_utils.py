# Standard library
import os, unittest, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Local
from brickulator import utils


class TestStringMethods(unittest.TestCase):

    def test_bricks_and_plates(self):
        # One plate == one plate
        self.assertTupleEqual((0, 1), utils.bricks_and_plates(1))
        # One brick == three plates
        self.assertTupleEqual((1, 0), utils.bricks_and_plates(3))
        # One brick, one plate == four plates
        self.assertTupleEqual((1, 1), utils.bricks_and_plates(4))

    def test_peg_perimeter1(self):
        expected_perimeter = 12
        actual_perimeter = utils.peg_perimeter([4, 4, 4, 4])
        self.assertEqual(expected_perimeter, actual_perimeter)

    def test_peg_perimeter2(self):
        expected_perimeter = 12
        actual_perimeter = utils.peg_perimeter([4, 4, 4, 4])
        self.assertEqual(expected_perimeter, actual_perimeter)
