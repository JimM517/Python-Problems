# 49 Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

from collections import defaultdict

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    # hashmap solution
    result = defaultdict(list)   #mapping charCount to a list of anagrams
    
    for s in strs:
        count = [0] * 26   # a - z
        
        for c in s:
            count[ord(c) - ord("a")] += 1
        
        result[tuple(count)].append(s)
    
    return result.values()


# O(m * n)
        