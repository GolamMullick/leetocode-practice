class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            if needle in haystack:
                return haystack.index(needle)
            else : 
                return -1
            
a = Solution()
b = a.strStr("sadbutsad","sad1")
print(b)