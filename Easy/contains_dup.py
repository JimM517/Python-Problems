# 217 Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.


# hash set solution
class Solution:
    
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        
        for n in nums:
            
            if n in hashset:
                return True
            hashset.add(n)
        return False
     