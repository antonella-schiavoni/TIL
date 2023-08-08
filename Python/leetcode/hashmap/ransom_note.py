# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

def canConstruct(ransomNote: str, magazine: str) -> bool:
  counter_ransomNote = Counter(ransomNote)
  counter_magazine = Counter(magazine)
  
  for key, value in counter_ransomNote.items():
      if key in counter_magazine.keys():
          if value > counter_magazine[key]:
              return False
      else:
          return False
  return True
