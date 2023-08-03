s = "the sky is blue"

class Solution:
    def reverseWords(self, s: str) -> str:
        splitted_s = s.split()
        join_s = " ".join(splitted_s[::-1])
        return join_s
        
solution = Solution()
print(solution.reverseWords(s))