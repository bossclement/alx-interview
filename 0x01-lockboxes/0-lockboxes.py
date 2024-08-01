#!/usr/bin/python3
"""
Module doc
"""


def can_open_all_boxes(boxes):
    """
    Determines if all boxes in a given list can be opened.

    Args:
        boxes: A list of lists, where each inner list represents the keys in a box.

    Returns:
        True if all boxes can be opened, False otherwise.
    """

    box_count = len(boxes)
    unlocked_boxes = set()

    for index, keys in enumerate(boxes):
        if not keys or index == 0:
            unlocked_boxes.add(index)
        for key in keys:
            if 0 <= key < box_count and key != index:
                unlocked_boxes.add(key)
        if len(unlocked_boxes) == box_count:
            return True
    return False
