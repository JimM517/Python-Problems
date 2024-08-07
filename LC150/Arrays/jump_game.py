# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums) - 1
        firstVal = nums[0]
        
        for i in range(m - 1, - 1, -1):
            if i + nums[i] >= m:
                m = i
                
        return m == 0
        
        
            
            