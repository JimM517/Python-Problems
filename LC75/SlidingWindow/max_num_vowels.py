# 1456. Maximum number of vowels in a substring of a given length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        left = 0
        
        max_vowel_count = vowel_count = sum(c in vowels for c in s[:k])

        for right in range(k, (len(s))):
            vowel_count += s[right] in vowels
            
            vowel_count -= s[left] in vowels
            
            left += 1
            
            max_vowel_count = max(max_vowel_count, vowel_count)
        
        return max_vowel_count
    
    
    

s = "abciiidef"
answer = Solution()
print(answer.maxVowels(s, 3))

