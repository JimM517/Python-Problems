# 918 maximum sum circular subarray
import math
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        curr_max_sum = 0
        curr_min_sum = 0
        max_sum = -math.inf
        min_sum = math.inf
        
        
        for num in nums:
            total_sum += num
            curr_max_sum = max(curr_max_sum + num, num)
            curr_min_sum = min(curr_min_sum + num, num)
            max_sum = max(max_sum, curr_max_sum)
            min_sum = min(min_sum, curr_min_sum)
        
        
        return max_sum if max_sum < 0 else max(max_sum, total_sum - min_sum)
    
    
    
    
    