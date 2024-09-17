#3. Longest substring without repeating characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sub_sets = set([])
        
        left = 0
        right = 0
        
        count = 0
        
        while right < len(s):
            if s[right] in sub_sets:
                sub_sets.remove(s[left])
                left += 1
            else:
                sub_sets.add(s[right])
                count = max(count, right - left + 1)
                right += 1
        
        return count
        
        
s = "bbbbb"

answer = Solution()

print(answer.lengthOfLongestSubstring(s))