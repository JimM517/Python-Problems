# 49. group anagrams
from collections import defaultdict
from typing import List



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count of each string to list of anagrams
        result = defaultdict(list)
        
        for s in strs:
            # initialize array count of length 26, all set to 0
            count = [0] * 26
    
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            result[tuple(count)].append(s)
    
        return result.values()