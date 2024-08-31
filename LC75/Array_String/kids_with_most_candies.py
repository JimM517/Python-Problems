# 1431. kids with the greatest number of candies
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        k = len(candies)
        maxCandy = 0
        
        result = []
        
        for candy in candies:
            maxCandy = max(maxCandy, candy)
            
        for x in range(0, k):
            if candies[x] + extraCandies >= maxCandy:
                result.append(True)
            else:
                result.append(False)
        
        return 




candies = [2, 3, 5, 1, 3]
extraCandies = 3


