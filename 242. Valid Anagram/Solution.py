s = "anagram"
t = "nagaram"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
solution = Solution()
print(solution.isAnagram(s, t))