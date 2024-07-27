# 169 Majority Element

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        
        for number in nums:
            if number in map:
                map[number] += 1
            else:
                map[number] = 1
                
        n = len(nums)
       
        for value in map:
            if map[value] > n // 2:
                return value




nums = [2,2,1,1,1,2,2]

sol = Solution()

print(sol.majorityElement(nums))





























