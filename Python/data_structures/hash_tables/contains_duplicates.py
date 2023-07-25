"""
Given an integer array nums, return true if any value appears at least twice in the
array, and return false if every element is distinct.

Examples:
---------

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from collections import defaultdict
from typing import List


def contains_duplicates(array: List) -> bool:
    """
    Function that checks if a list contains duplicates.

    Time complexity is O(n) because it has to iterate through each element in the
    array once to convert it to a set.

    Space complexity is O(n) because in the worst case scenario a set of equal size
    to the array is created.
    """
    set_array = set(array)

    if len(set_array) < len(array):
        return True
    else:
        return False


def contains_duplicates_with_dic(array: List) -> bool:
    """
    Function that checks if a list contains duplicates. This one uses a dictionary to
    store the numbers and the frequency of each number.

    Time complexity is O(n) because it has to iterate through each element in the
    array once.

    Space complexity is O(n) because in the worst case scenario all the elements are
    unique.
    """
    number_to_frequency = defaultdict(int)

    for number in array:
        if number in number_to_frequency.keys():
            return True
        else:
            number_to_frequency[number] += 1
    return False


if __name__ == "__main__":
    print(contains_duplicates([1, 2, 3, 1]))
