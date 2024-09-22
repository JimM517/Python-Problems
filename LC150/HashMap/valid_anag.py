# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map, t_map = {}, {}
        
        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
            
        
        for char in s_map:
            if s_map[char] != t_map.get(char, 0):
                return False
        return True




s = "anagram"
t = "nagaram"

answer = Solution()

print(answer.isAnagram(s, t))


