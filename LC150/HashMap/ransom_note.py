# 383. ransom note


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = {}

        for ch in magazine:
            if ch not in ransom_map:
                ransom_map[ch] = 1
            else:
                ransom_map[ch] += 1
        
        for ch in ransomNote:
            if ch in ransom_map and ransom_map[ch] > 0:
                ransom_map[ch] -= 1
            else:
                return False
        return True
    
    

ransomNote = "aa"
magazine = "aab"

answer = Solution()

print(answer.canConstruct(ransomNote, magazine))


