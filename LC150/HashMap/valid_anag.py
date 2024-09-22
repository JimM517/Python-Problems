# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map, t_map = {}, {}
        
        for i,j in len(s) and len(t):
            s_map[i] = 1 + s_map.get(s[i], 0)
            t_map[j] = 1 + t_map.get(t[j], 0)
            
        
        for char in s_map:
            if s_map[char] != t_map.get(char, 0):
                return False
        return True




s = "rat"
t = "car"

answer = Solution()

print(answer.isAnagram(s, t))


