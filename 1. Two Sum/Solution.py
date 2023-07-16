nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        my_dict = {}
        for index, num in enumerate(nums):
            if (target - num) in my_dict:
                return [my_dict[target - num], index]
            else:
                my_dict[num] = index

solution = Solution()
print(solution.twoSum(nums, target))