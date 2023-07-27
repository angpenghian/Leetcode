from typing import List

nums = [3,2,2,3]
val = 3

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
                print(nums)
        print(nums)
        return index
        
solution = Solution()
print(solution.removeElement(nums,val))