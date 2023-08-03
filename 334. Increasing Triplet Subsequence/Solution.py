from typing import List

nums = [20,100,10,12,5,13]



class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for middle in range(1, len(nums) - 1):
            left = middle - 1
            right = middle + 1
            if (nums[left] < nums[middle] < nums[right]):
                return True
        
        
        
solution = Solution()
print(solution.increasingTriplet(nums))