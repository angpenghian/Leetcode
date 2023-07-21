from typing import List

nums = [1,1,2]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = []
        num_set = set()

        for num in nums:
            if num not in num_set:
                unique_nums.append(num)
                num_set.add(num)
                
        return (unique_nums)
        
        
solution = Solution()
print(solution.removeDuplicates(nums))