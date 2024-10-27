# 20. valid parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' or c == '}' or c == ']':
                if len(stack) == 0:
                    return False

                top = stack.pop()
                
                if (c == ')' and top != '(') or (c == '}' and top != '{') or c == ']' and top != '[':
                    return False
        
        return not stack
                
        
        
s = "()[]{}"

answer = Solution()

print(answer.isValid(s))
        