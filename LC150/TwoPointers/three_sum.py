# 15. 3Sum
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        nums.sort()
        
        n = len(nums) - 2
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total > 0:
                   k -= 1
                elif total < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j - 1] == nums[j] and j < k:
                        j += 1
        
        return result
                    
        
nums = [-1,0,1,2,-1,-4]
answer = Solution()
print(answer.threeSum(nums))