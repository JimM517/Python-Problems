# 1493 longest subarray of 1's after deleting one element
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        prevWindow = 0
        currWindow = 0
        
        window_max = 0
        
        for i in range(0, len(nums)):
            if nums[i] == 0:
                window_max = max(window_max, prevWindow + currWindow)
                prevWindow = currWindow
                currWindow = 0
            else:
                currWindow += 1
        
        if currWindow == len(nums):
            return currWindow - 1
        
        
        window_max = max(window_max, prevWindow + currWindow)
        
        return window_max
    
    


nums = [1, 1, 0, 1]  

answer = Solution()
print(answer.longestSubarray(nums))
