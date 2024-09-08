# 151. reverse words in a string

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        result = ""
        
        for i in range(len(arr) -1, -1, -1):
            result += arr[i]
            
            if i > 0:
                result += " "
        
        return result
    


sol = Solution()

s = "the sky is blue"
        
print(sol.reverseWords(s))
        