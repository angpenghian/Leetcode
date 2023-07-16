from typing import List

prices = [7,1,5,3,6,4]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        maxprofit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
            else:
                left = right
            right += 1
            
        return maxprofit
        
        
solution = Solution()
print(solution.maxProfit(prices))