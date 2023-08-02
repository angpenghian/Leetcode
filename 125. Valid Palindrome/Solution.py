s = "A man, a plan, a canal: Panama"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i  in s.lower():
            if i.isalnum() == False:
                pass
            else:
                string += i.lower()
                
        if (string == string[::-1]):
            return True
        else:
            return False
        
solution = Solution()
print(solution.isPalindrome(s))