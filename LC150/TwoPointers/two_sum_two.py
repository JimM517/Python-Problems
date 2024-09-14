# 167. Two Sum II - input array is sorted
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        while start < end:
            tar_sum = numbers[start] + numbers[end]
            
            if tar_sum > target:
                end -= 1
            elif tar_sum < target:
                start += 1
            else:
                return [start + 1, end + 1]
        
        
        return None
    

numbers = [2, 3, 4]
target = 6

sol = Solution()

print(sol.twoSum(numbers, target))

