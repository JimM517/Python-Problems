# 13. Roman to Integer



class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        number = 0
        
        for i in range(len(s) - 1):
            if map[s[i]] < map[s[i + 1]]:
                number -= map[s[i]]
            else:
                number += map[s[i]]
        
        return number + map[s[-1]]


s = 'LVIII'

sol = Solution()

print(sol.romanToInt(s))


    