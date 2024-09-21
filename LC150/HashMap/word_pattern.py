# 290. word pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        arr = s.split(' ')
        
        if len(pattern) != len(arr):
            return False
        
        
        char_word, word_char = {}, {}
        
        for i in range(len(pattern)):
            ch = pattern[i]
            word = arr[i]
            
            if ch in char_word:
                if char_word[ch] != word:
                    return False
            else:
                if word in word_char and word_char[word] != ch:
                    return False
                
                char_word[ch] = word
                word_char[word] = ch
        
        return True
    
            
            
            
            
            
            
            
    
pattern = "abba"
s = "dog cat cat dog"

answer = Solution()

print(answer.wordPattern(pattern, s))

