# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=trees
class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


def decodeHuff(root, s):
    """
    Space complexity: O(s), with s being the length of the string
    Time complexity: O(n)
    """
    output = ""
    node = root
    for i in range(len(s)):
        if s[i] == '0':
            node = node.left
        else:
            node = node.right
        if node.left is None and node.right is None:  # it's a leaf node
            output += node.data
            node = root
    return output
