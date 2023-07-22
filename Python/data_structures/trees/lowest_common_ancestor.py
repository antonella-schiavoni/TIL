class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def lca(root, v1, v2):
    """
    Complexity of this function is O(n) in the worst case, as it may traverse all the
    nodes in the binary search tree.
    """

    # Base case
    if root is None:
        return 0
    if v1 == root.info or v2 == root.info:
        return root

    # Look for v1 and v2 in left and right subtrees
    left = lca(root.left, v1, v2)
    right = lca(root.right, v1, v2)

    # If both of the above calls return Non-NULL, then one value is present in
    # one subtree and the other is present in another. So, this node is the LCA.
    if left and right:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left if left is not None else right


def lca_improved(root, v1, v2):
    """
    There is a more efficient way to find the lowest common ancestor (LCA) due to the
    property of BSTs that for any given node, all nodes in the left subtree are smaller
    and all nodes in the right subtree are larger.
    """

    # Base case
    if root is None:
        return None

    # If both v1 and v2 are smaller than root, then LCA lies in left
    if root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)

    # If both v1 and v2 are greater than root, then LCA lies in right
    if root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)

    return root


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = 8

    arr = list(map(int, "8 4 9 1 2 3 6 5".split()))

    for i in range(t):
        tree.create(arr[i])

    v = list(map(int, "1 2".split()))

    ans = lca(tree.root, v[0], v[1])
    print(ans.info)
