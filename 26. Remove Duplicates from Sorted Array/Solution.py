from typing import List

nums = [1,1,2]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replace = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[replace] = nums[i]
                replace += 1
        return replace
    
solution = Solution()
print(solution.removeDuplicates(nums))