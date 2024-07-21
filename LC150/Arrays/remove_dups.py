# 26. remove duplicates from sorted array


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
                
        return k
        
                


# nums = [1, 1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]

sol = Solution()

print(sol.removeDuplicates(nums))















