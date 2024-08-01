#!/usr/bin/python3
"""
Module doc
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes in a given list can be opened.

    Args:
        boxes: A list of lists, where each inner list represents the keys in a box.

    Returns:
        True if all boxes can be opened, False otherwise.
    """

    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
