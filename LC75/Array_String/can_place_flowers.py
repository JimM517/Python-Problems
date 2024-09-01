# 605. Can place flowers
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        
        if n == 0:
            return True
        
        for i in range(0, size):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == size - 1 or flowerbed[i + 1] == 0):
                n -= 1
                if n == 0:
                    return True
                flowerbed[i] = 1
        
        return False
    

sol = Solution()

flowerbed = [1, 0, 0, 0, 1]

print(sol.canPlaceFlowers(flowerbed, 2))

