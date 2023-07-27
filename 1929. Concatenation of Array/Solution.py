from typing import List

nums = [1,2,1]

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return (nums + nums)
    
solution = Solution()
print(solution.getConcatenation(nums))