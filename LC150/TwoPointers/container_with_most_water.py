# 11. container with most water
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_height = 0

        while left < right:
            h = right - left
            w = min(height[left], height[right])
            area = w * h
            
            max_height = max(max_height, area)
            
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
            
        return max_height
    

height = [1,8,6,2,5,4,8,3,7]

answer = Solution()

print(answer.maxArea(height))

