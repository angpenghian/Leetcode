from typing import List

nums = [1,7,3,6,5,6]

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        
        for i in range(len(nums)):
            rightsum = total - nums[i] - leftsum
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1
    

solution = Solution()
print(solution.pivotIndex(nums))