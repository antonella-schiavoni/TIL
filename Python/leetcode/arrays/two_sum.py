from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Time complexity: O(n)
    """
    for i_0 in range(len(nums) - 1):
        # This iterates from index 0 to len(nums) - 1
        for i_1 in range(1, len(nums)):
            if nums[i_0] + nums[i_1] == target and i_1 != i_0:
                return [i_0, i_1]


def twoSum_optimized(nums: List[int], target: int) -> List[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    num_idx = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_idx:
            return [num_idx[complement], idx]
        num_idx[num] = idx


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 17], 9))
    print(twoSum([3, 2, 4], 6))
