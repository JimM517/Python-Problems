# 2215. find the difference of two arrays
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        num_one_map = {}
        num_two_map = {}
        
        for num in nums1:
            num_one_map[num] = num_one_map.get(num, 0) + 1
        
        for num in nums2:
            num_two_map[num] = num_two_map.get(num, 0) + 1
        
        
        num_one_list = []
        num_two_list = []
        result = []
        
        for key, value in num_one_map.items():
            if key not in num_two_map:
                num_one_list.append(key)
        
        for key, value in num_two_map.items():
            if key not in num_one_map:
                num_two_list.append(key)
                
        result.append(num_one_list)
        result.append(num_two_list)
        
        return result


nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

answer = Solution()

print(answer.findDifference(nums1, nums2))


            
        
        