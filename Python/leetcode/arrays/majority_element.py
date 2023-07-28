"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may
assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""
from collections import Counter
from typing import List


def majorityElement(nums: List[int]) -> int:
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    number_to_frequency = Counter(nums)
    max_frequency = max(number_to_frequency.items(), key=lambda x: x[1])
    return max_frequency[0]


if __name__ == "__main__":
    # Test cases
    majorityElement([3, 2, 3])
    majorityElement([2, 2, 1, 1, 1, 2, 2])
