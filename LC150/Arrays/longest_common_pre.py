#14 Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string ""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""
        
        n = len(strs)
        
        strs.sort()
        
        for i in range(len(strs[0])):
            if strs[0][i] == strs[n - 1][i]:
                result += strs[0][i]
            else:
                break
        
        return result
        
        

strs = ['flower', 'flow', 'flight']

sol = Solution()

print(sol.longestCommonPrefix(strs))

