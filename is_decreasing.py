# Author: Joseph Serra
# GitHub username: jserra99
# Date: 11/2/2023
# Description: Project-6b; Is Decreasing

def is_decreasing(num_list: list[float]):
    """ Returns true if the given list is strictly decreasing, returns false otherwise. """
    if len(num_list) == 2:
        return num_list[1] < num_list[0]
    return num_list[1] < num_list[0] and is_decreasing(num_list[1:])
