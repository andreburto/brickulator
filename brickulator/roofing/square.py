# Local imports
from brickulator.utils import peg_perimeter

# All functions in this file assume the roof is a square.
ROOFING_SIDES = 4
# The smallest widths of a four-sided roof which would require corner slopes.
MINIMUM_SIZE_FOR_CORNERS = [4, 4, 4, 4]


def peg_width_per_levels(base_width):
    """ Calculates how many pegs wide each level of a side will be. """
    limiter = 2
    decrementer = -2
    decrementing_width = int(base_width)
    peg_count_per_level = []
    while decrementing_width >= limiter:
        peg_count_per_level.append(int(decrementing_width))
        decrementing_width += decrementer
    return peg_count_per_level


def corners_per_level(side_lengths):
    # If the sum of the sides minus the sides is not greater than the sides there's no need for corner bricks
    # TODO: Define a better condition for calculating corners.
    # TODO: Account for 3x3 corners and other slope angles.
    return len(side_lengths) if peg_perimeter(side_lengths) >= peg_perimeter(MINIMUM_SIZE_FOR_CORNERS) else 0


def slope_bricks_per_level_per_side(side_length):
    """ Calculates the number of 4, 2, and 1 width non-corner, sloped bricks per level. """
    # Get the number of 4x2 slope bricks needed.
    four_brick_count = int(side_length / 4)
    remainder_bricks = side_length % 4 if side_length > 0 else 0
    # Calculate the remainder bricks you need.
    remainder_two_bricks = 1 if remainder_bricks > 1 else 0
    remainder_one_bricks = remainder_bricks % 2
    return four_brick_count, remainder_two_bricks, remainder_one_bricks


def slope_bricks_per_level(side_lengths):
    corner_bricks = corners_per_level(side_lengths)
    four_bricks = 0; two_bricks = 0; one_bricks = 0
    for side_length in side_lengths:
        # Each side has four pegs dedicated to corner slopes.
        sans_corners = side_length - 4
        four_bricks, two_bricks, one_bricks = tuple(map(sum, zip((four_bricks, two_bricks, one_bricks),
                                                                 slope_bricks_per_level_per_side(sans_corners))))
    return corner_bricks, int(four_bricks), int(two_bricks), int(one_bricks)


def bricks_per_square_roof(base_width):
    """ Calculates all the bricks you need to make a square, 90 degree roof. """
    corner_bricks = 0; four_bricks = 0; two_bricks = 0; one_bricks = 0
    for level_length in peg_width_per_levels(base_width):
        four_sides = [level_length for x in range(ROOFING_SIDES)]
        corner_bricks, four_bricks, two_bricks, one_bricks = tuple(map(sum, zip(slope_bricks_per_level(four_sides),
                                                                                (corner_bricks, four_bricks, two_bricks,
                                                                                 one_bricks))))
    return corner_bricks, four_bricks, two_bricks, one_bricks
