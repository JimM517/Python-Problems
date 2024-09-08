# 443. string compression
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        
        for i in range(len(chars) -1, -1, -1):
            if i and chars[i] == chars[i - 1]:
                count += 1
                chars.pop()
            else:
                if count > 1:
                    for x in str(count)[::-1]:
                        chars.insert(i + 1, x)
                    count = 1
        return len(chars)



sol = Solution()
chars = ["a","a","b","b","c","c","c"]
print(sol.compress(chars))