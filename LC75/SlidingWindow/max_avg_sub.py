# 643. maximum average subarray
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> int:
        
        total = 0
        
        for i in range(k):
            total += nums[i]
        
        
        max_total = total
        
     
        
        for j in range(k, len(nums)):
            total = total + nums[j] - nums[j - k]
            
            max_total = max(max_total, total)
        
        return max_total / k
    
    


nums = [1,12,-5,-6,50,3]
answer = Solution()

print(answer.findMaxAverage(nums, 4))