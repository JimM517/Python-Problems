# 205. isomorphic strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dict1, dict2 = {}, {}
        
        for s1, t1 in zip(s, t):
            if (s1 in dict1 and dict1[s1] != t1) or (t1 in dict2 and dict2[t1] != s1):
                return False

            dict1[s1] = t1
            dict2[t1] = s1
            
        return True


s = "foo"
t = "bar"

answer = Solution()

print(answer.isIsomorphic(s, t))



        