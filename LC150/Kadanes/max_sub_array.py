# 53. maximum subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = float("-inf")
        end = 0
        
        for num in nums:
            end += num
            
            if start < end:
                start = end
            
            if end < 0:
                end = 0
    
        return start
    
nums = [5,4,-1,7,8]

answer = Solution()

print(answer.maxSubArray(nums))


