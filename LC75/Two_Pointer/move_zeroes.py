# 238. Move zeroes
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        start = 0
        end = len(nums)
        
        for x in range(end):
            if nums[x] != 0:
                nums[start], nums[x] = nums[x], nums[start]
                start += 1
            print(nums)


sol = Solution()
nums = [0, 1, 0, 3, 12]

sol.moveZeroes(nums)