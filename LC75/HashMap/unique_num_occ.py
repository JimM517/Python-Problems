# 1207. unique number of occurrences
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}
        
        
        for num in arr:
            count_map[num] = count_map.get(num, 0) + 1
        
        

        if len(set(count_map.values())) != len(set(arr)):
            return False
        
        return True
    