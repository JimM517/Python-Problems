# 189 Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative
from typing import List



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # get number of rotations
        k = k % len(nums)
        
        # get number of elements to move from end to beginning
        r = len(nums) - k
        
        # store elements to move
        temp = nums[0:r]
        
        # remove elements from the beginning
        nums[0:r] = []
       
        # append stored elements to the end
        nums.extend(temp)
      



nums = [1,2,3,4,5,6,7]  
    
    
sol = Solution()
print(sol.rotate(nums, 3))