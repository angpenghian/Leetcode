s = "luffy is still joyboy"

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_string = s.split()
        return(len(split_string[-1]))
    
solution = Solution()
print(solution.lengthOfLastWord(s))