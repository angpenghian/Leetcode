x = 1000021

class Solution:
    def isPalindrome(self, x: int) -> bool:
        normal_string = str(x)
        reversed_string = (str(x))[::-1]
        true_or_false = True
        for index, i in enumerate (normal_string):
            if normal_string[index] == reversed_string[index]:
                true_or_false = True
            else:
                true_or_false = False
                break
        return true_or_false
            
solution = Solution()
print(solution.isPalindrome(x))