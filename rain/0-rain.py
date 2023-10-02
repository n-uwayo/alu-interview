#!/usr/bin/python3
"""
Given a list of non-negative integers representing walls of width 1,
calculate how much water will be retained after it rains.
"""


def rain(walls):
    """
    Calculate the amount of water that can be retained after rainfall.

    Args:
        walls (list of int): A list of non-negative integers
        representing wall heights.

    Returns:
        int: The total amount of water that can be retained between the walls.
             Returns 0 for empty input.

    Example:
        >>> rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        6

    """
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    max_left, max_right = walls[left], walls[right]
    total = 0

    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, walls[left])
            total += max_left - walls[left]
        else:
            right -= 1
            max_right = max(max_right, walls[right])
            total += max_right - walls[right]

    return total
