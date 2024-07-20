# 27. Remove element


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        for num in nums:
            if num is not val:
                nums[i] = num
                i += 1
        
        return i






# nums = [3, 2, 2, 3]
nums = [0,1,2,2,3,0,4,2]

sol = Solution()

print(sol.removeElement(nums, 2))






