# 724. find the pivot index
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        
        if n == 0:
            return -1
        
        
        leftSum = 0
        rightSum = 0
        
        for i in range(n):
            rightSum += nums[i]
            

        for i in range(n):
            rightSum -= nums[i]
            
            if rightSum == leftSum:
                return i
            
            leftSum += nums[i]
            
        return -1
    
    

answer = Solution()
nums = [2,1,-1]

print(answer.pivotIndex(nums))