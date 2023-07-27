from typing import List

nums = [0,1,0,3,12]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        return (nums)
        
        

solution = Solution()
print(solution.moveZeroes(nums))