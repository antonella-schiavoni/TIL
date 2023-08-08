# https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150

def climbStairs(n: int) -> int:
  if n <= 2:
      return n
  a, b = 1, 2
  for _ in range(n - 2):
      a, b = b, a + b
  return b
