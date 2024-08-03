# 274 H-Index

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort()
        
        # for i in range(len(citations)):
        #     h = len(citations) - i
            
        #     if citations[i] >= h:
        #         return h
        
        # return 0
        
        
        #### another solution ####
        citations.sort(reverse=True)
        n = len(citations)
        h = 0
        
        for i in range(n):
            if citations[i] >= i + 1:
                h = i + 1
        
        return h
    




citations = [3, 0, 6, 1, 5]

sol = Solution()


print(sol.hIndex(citations))















