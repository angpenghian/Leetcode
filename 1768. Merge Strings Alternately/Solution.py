word1 = "ab"
word2 = "pqrs"

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ""
        word1_len = 0
        word2_len = 0
        while word1_len < len(word1) or word2_len < len(word2):
            if word1_len < len(word1):
                mergedString += word1[word1_len]
                word1_len += 1
            if word2_len < len(word2):
                mergedString += word2[word2_len]
                word2_len += 1
        return mergedString

        
solution = Solution()
print(solution.mergeAlternately(word1, word2))