from typing import List

digits = [1,2,3]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        joined_digits = ''.join(str(digit) for digit in digits)
        joined_digits = int(joined_digits) + 1
        split_digits = [int(digit) for digit in str(joined_digits)]
        return split_digits
        


solution = Solution()
print(solution.plusOne(digits))