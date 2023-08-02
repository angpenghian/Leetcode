from typing import List

numbers = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, num in enumerate(numbers):
            if (target - num) in my_dict:
                return [my_dict[target - num] + 1 , index + 1]
            else:
                my_dict[num] = index
                
solution = Solution()
print(solution.twoSum(numbers, target))