from typing import List

s = "leetcodeisacommunityforcoders"

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        output = ""
        for i in s:
            if i not in vowels:
                output += i
        return output
        
        

solution = Solution()
print(solution.removeVowels(s))