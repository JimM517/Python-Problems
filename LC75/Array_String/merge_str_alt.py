#1768. merge strings alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        
        result = ''
        
        i = 0
        
        while i < n and i < m:
            result += word1[i]
            result+= word2[i]
            i += 1
            
        while i < n:
            result += word1[i]
            i += 1
        
        while i < m:
            result += word2[i]
            i += 1
        
        return result


word1 = "abc"
word2 = "pqr"

sol = Solution()


print(sol.mergeAlternately(word1, word2))


