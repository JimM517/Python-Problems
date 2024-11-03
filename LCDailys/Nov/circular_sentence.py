# 2490. circular sentence


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        for i in range(len(sentence)):
            if sentence[i] == " ":
                if (sentence[i - 1] != sentence[i + 1]):
                    return False

        
        return sentence[0] == sentence[len(sentence) - 1]





sentence = "Leetcode is cool"

answer = Solution()

print(answer.isCircularSentence(sentence))



