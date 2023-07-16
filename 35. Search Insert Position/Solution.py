from typing import List

nums = [1,3,5,6]
target = 7

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        target_index = 0
        
        for i in nums:
            if i == target:
                target_index = nums.index(i)
            elif i < target:
                    target_index = nums.index(i) + 1
        return target_index
            
solution = Solution()
print(solution.searchInsert(nums, target))