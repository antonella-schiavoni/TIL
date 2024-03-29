# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    For a Binary Tree (not necessarily a Binary Search Tree). 
    This logic does not use the properties of BST, so it needs to search in both left and right subtrees before determining the LCA.
    """
    if not root or root == p or root == q:
        return root
    
    l = self.lowestCommonAncestor(root.left, p, q)
    r = self.lowestCommonAncestor(root.right, p, q)
    
    if l and r:
        return root
    return l or r
