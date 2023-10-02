#!/usr/bin/python3
"""
Given a list of non-negative integers representing walls of width 1,
calculate how much water will be retained after it rains.
"""


def rain(walls):
  """
    Function that gets the water drop from walls.

    Args:
        param1: walls wallsay structure.

    Returns:
        The water inside walls

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
