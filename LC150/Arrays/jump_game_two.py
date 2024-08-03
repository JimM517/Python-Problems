# 45. jump game II

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1]
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:
        end = 0
        maxJump = 0
        steps = 0
        
        for i in range(len(nums) - 1):
            maxJump = max(maxJump, i + nums[i])
            
            if i == end:
                end = maxJump
                steps += 1
        
        return steps





nums = [2, 3, 1, 1, 4]

sol = Solution()

print(sol.jump(nums))






