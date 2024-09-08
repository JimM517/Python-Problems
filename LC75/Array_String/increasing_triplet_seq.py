# 334. increasing triplet subsequence
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        
        return False
    
    

nums = [5, 4, 3, 2, 1]

sol = Solution()

print(sol.increasingTriplet(nums))
