# 1004. max consecutive ones III
from typing import List



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        start = 0
        end = 0
        
        zeros = 0
        
        while end < len(nums):
            if nums[end] == 0:
                zeros += 1
            end += 1
            
            if zeros > k:
                if nums[start] == 0:
                    zeros -= 1
                start += 1

        return end - start
    
    
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]

answer = Solution()
print(answer.longestOnes(nums, 3))


