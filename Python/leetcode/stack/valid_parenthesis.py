# https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

def isValid(self, s: str) -> bool:
  stack = []
  close_to_open = {"]": "[", ")": "(", "}": "{"}
  
  for char in s:
      if char in close_to_open.values():  # If the character is an opening bracket
          stack.append(char)
      elif char in close_to_open:  # If the character is a closing bracket
          if not stack or stack.pop() != close_to_open[char]:
              return False
  
  return len(stack) == 0
