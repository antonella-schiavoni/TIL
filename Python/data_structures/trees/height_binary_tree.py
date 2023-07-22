# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=trees
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):

    # base case: empty node
    if root is None:
        return -1
    left_heigh = height(root.left)
    right_heigh = height(root.right)
    
    return max(left_heigh, right_heigh) + 1
