# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/?envType=study-plan-v2&envId=top-interview-150


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_height = self.maxDepth(root.left) + 1
    right_height = self.maxDepth(root.right) + 1
    return max(left_height, right_height)
