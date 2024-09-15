# 209. Minimum size subarray sum
from typing import List
from sys import maxsize

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = maxsize
        left, total = 0, 0
        n = len(nums)
        
        for i in range(n):
            total += nums[i]
            
            while total >= target:
                result = min(result, i - left + 1)
                total -= nums[left]
                left += 1
        
        return result if result != maxsize else 0


