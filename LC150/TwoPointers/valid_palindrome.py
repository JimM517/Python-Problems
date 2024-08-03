# 125. valid palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise

class Solution:
    def isPalindrome(self, s: str) -> bool:
    # converts s to lower case and only includes alphanumeric characters
    # then compares s to its reverse
    #    s = [i for i in s.lower() if i.isalnum()]
    #    return s == s[::-1]
   
    
    #### two pointer approach ####
        i = 0
        j = len(s) - 1
        
        while i < j:
            a = s[i].lower()
            b = s[j].lower()
            
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i += 1
                    j -= 1
                    continue
            i = i + (not a.isalnum())
            j = j - (not b.isalnum())
        
        return True
    
       


s = "race a car"

sol = Solution()

print(sol.isPalindrome(s))


