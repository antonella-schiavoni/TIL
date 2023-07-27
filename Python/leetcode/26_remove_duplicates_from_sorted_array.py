"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
def removeDuplicates(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not nums:
        return 0
    unique_pointer = 1
    for fast_pointer in range(1, len(nums)):
        if nums[fast_pointer] != nums[fast_pointer - 1]:
            nums[unique_pointer] = nums[fast_pointer]
            unique_pointer += 1
    print(nums[:unique_pointer])
    return unique_pointer
