# Author: Joseph Serra
# GitHub username: jserra99
# Date: 11/2/2023
# Description: Project-6b; Is Decreasing

def is_decreasing(num_list: list[float]):
    """ Returns true if the given list is strictly decreasing, returns false otherwise. """
    comparison = num_list.pop(0)
    for number in num_list:
        if number >= comparison:
            return False
        comparison = number
    return True
