# 1732. find the highest altitude
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        curr_alt = 0
        max_alt = 0
        
        for i in range(0, len(gain)):
            curr_alt += gain[i]
            max_alt = max(max_alt, curr_alt)
        
        return max_alt
            
            
            

gain = [-4,-3,-2,-1,4,3,2]

answer = Solution()

print(answer.largestAltitude(gain))