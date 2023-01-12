
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return "True"
        else:
            return "False"
        
a = Solution()
b = a.isAnagram("cat", "abt")

print(b) 