# https://leetcode.com/problems/invert-binary-tree/submissions/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return

    left = self.invertTree(root.right)
    right = self.invertTree(root.left)   
    root.left, root.right = root.right, root.left
    return root
