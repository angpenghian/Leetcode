from typing import List

nums = [1,1,1,2,2,3]
k = 2

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        sorted_num_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
        top_k_nums = []
        for i in range(k):
            top_k_nums.append(sorted_num_dict[i][0])
        
        return (top_k_nums)
        
        
solution = Solution()
print(solution.topKFrequent(nums, k))