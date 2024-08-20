# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        my_stack = []
        
        new_arr = s.split()
        
        for x in range((len(new_arr))):
            my_stack.append(new_arr[x])
        
        
        last_word = len(my_stack.pop())
        
        return last_word
    
        

s = 'Hello World'

sol = Solution()


print(sol.lengthOfLastWord(s))


        