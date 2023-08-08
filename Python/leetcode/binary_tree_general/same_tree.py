# https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
  if not p and not q:
      return True
  if not p or not q:
      return False
  
  if p.val != q.val:
      return False
      
  same_left = self.isSameTree(p.left, q.left)
  same_right = self.isSameTree(p.right, q.right)
  
  return same_left and same_right
