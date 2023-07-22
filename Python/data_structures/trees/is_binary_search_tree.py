# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=trees

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    """
    The time complexity of the solution is O(N), where N is the number of nodes in the
    tree. This is because worst-case scenario, we visit each node once. The time
    complexity is proportional to the size of the tree.
    """
    if root.data is None or root.left.data in None or root.right.data is None:
        return True

    if root.data > root.left.data:
        left = checkBST(root.left)
    else:
        return False
    if root.data < root.right.data:
        right = checkBST(root.right)
    else:
        return False
    return left and right


def check_bts_improved(root):
    """
    It checks that all values in a node's left subtree are less than the node's value,
    and all values in the node's right subtree are greater than the node's value.

    The time complexity is directly proportional to the number of nodes in the tree,
    which is O(N).
    """
    def is_BST(node, min_val, max_val):
        if node is None:
            return True
        if not min_val < node.data < max_val:
            return False
        return is_BST(node.left, min_val, node.data) and is_BST(node.right, node.data,
                                                                max_val)

    return is_BST(root, float('-inf'), float('inf'))
