# Standard library imports
from math import floor

# The number of plates stacked that equal the same height as a brick.
PLATES_IN_BRICK = 3


def bricks_and_plates(plates):
    """ Convert a number of plates into the total number of bricks and plates remainder. """
    if plates < PLATES_IN_BRICK:
        return 0, plates
    else:
        bricks = int(floor(plates / PLATES_IN_BRICK))
        plates_remainder = plates % PLATES_IN_BRICK
        return bricks, plates_remainder


def peg_perimeter(side_lengths):
    """ Calculates how many pegs in length the full parameter is. """
    return sum(side_lengths) - len(side_lengths)
