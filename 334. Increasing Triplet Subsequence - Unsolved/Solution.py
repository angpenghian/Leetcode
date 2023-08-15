from typing import List

nums = [20, 100, 10, 12, 5, 13]

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize first and second elements of the triplet to infinity
        first_element = float('inf')
        second_element = float('inf')
        
        # Iterate through the list
        for num in nums:
            # If the current number is less than or equal to the first element of the triplet, update the first element
            if num <= first_element:
                first_element = num
            # If the current number is greater than the first element but less than or equal to the second, update the second element
            elif num <= second_element:
                second_element = num
            # If the current number is greater than both first and second elements, we have found an increasing triplet
            elif num > second_element:
                return True
        
        # If we have iterated through the entire list and not found a triplet, return False
        return False

solution = Solution()
print(solution.increasingTriplet(nums))