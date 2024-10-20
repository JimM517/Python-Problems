# 128 longest consecutive sequence
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        longest = 0
        
        for n in nums:
            
            if (n - 1) not in num_set:
                length = 0
                
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        
        return longest