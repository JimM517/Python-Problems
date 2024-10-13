# 202 happy number


class Solution:
    def isHappy(self, n: int) -> bool:
        
        result = {}
        
        while n != 1 and n not in result:
            result[n] = 0
            
            
            num_str = str(n)
            
            total = 0
            
            for i in range(len(num_str)):
                digit = int(num_str[i])
                
                total += digit * digit
            
            n = total
                
                
        return n == 1
    
    
    