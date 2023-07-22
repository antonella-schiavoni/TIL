# https://leetcode.com/problems/merge-sorted-array/description/
class Solution:
  """
  The time complexity of merge() is given by the sort function. Sort uses Timsort which has an average worst case time complexity of O(n log n), where n is the length of the list being sorted (in this case is n + m)
  The space complexity of merge() is O(1), because it only uses a constant amount of additional space to store the loop variable i. As it does not create any new list, it does not afferct. Sort does not also affect because it's an inplace method.
  
  """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,m+n):
            nums1[i]=nums2[i-m]
        nums1.sort()



# Solution in O(m+n) time
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        # if there are still elements left in nums2
        if n > 0:
            nums1[:n] = nums2[:n]
