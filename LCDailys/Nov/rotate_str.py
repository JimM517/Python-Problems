# 796 rotate string


class Solution:
    def rotateString(self, s: str, goal: str):
        
        if len(s) != len(goal):
            return False
        
        return goal in s + s
    

s = "abcde"
goal = "cdeab"

answer = Solution()

print(answer.rotateString(s, goal))


