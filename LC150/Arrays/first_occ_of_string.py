# 28. find the index of the first occurence in a string
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
      
    
    

haystack = "sadbutsad"
needle = "sad"

sol = Solution()

print(sol.strStr(haystack, needle))

