from typing import List

nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i + m] = nums2[i]
        
        # Sort nums1 list in-place.
        nums1.sort()
            
        
        
        
solution = Solution()
print(solution.merge(nums1, m, nums2, n))