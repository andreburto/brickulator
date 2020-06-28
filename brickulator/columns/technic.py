# Local imports
from ..utils import bricks_and_plates


# The number of plates and technic holes BETWEEN the holes that use a connection.
PLATE_TO_HOLE_RATIO_DICT = {
    'plate': 5,
    'hole': 2,
}

#
PLATE_TO_HOLE_MIN_DICT = {
    'plate': 2,
    'hole': 1,
}


def increase_numbers(current_numbers_dict):
    """ Increment by one ratio set. """
    new_hole_amt = current_numbers_dict['hole'] + PLATE_TO_HOLE_RATIO_DICT['hole']
    new_plate_amt = current_numbers_dict['plate'] + PLATE_TO_HOLE_RATIO_DICT['plate']
    return {
        'hole': new_hole_amt,
        'plate': new_plate_amt,
    }


def decrease_numbers(current_numbers_dict):
    """ Decrease by one ratio set. Cannot go below the minimum ratio. """
    new_hole_amt = current_numbers_dict['hole'] - PLATE_TO_HOLE_RATIO_DICT['hole']
    new_plate_amt = current_numbers_dict['plate'] - PLATE_TO_HOLE_RATIO_DICT['plate']
    if new_hole_amt < PLATE_TO_HOLE_MIN_DICT['hole']:
        return PLATE_TO_HOLE_MIN_DICT
    else:
        return {
            'hole': new_hole_amt,
            'plate': new_plate_amt,
        }
