#219 contains duplicates two
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = {}
        
        
        for i in range(len(nums)):
            
            num = nums[i]
            
            
            if num in result and i - result[num] <= k:
                return True
            
            result[num] = i
            
            
        return False
    