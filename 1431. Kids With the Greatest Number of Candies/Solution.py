from typing import List

candies = [2,3,5,1,3]
extraCandies = 3

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        final_list = []
        for i in range(len(candies)):
            new_candie = candies[i] + extraCandies
            if new_candie < max(candies):
                final_list.append(False)
            else:
                final_list.append(True)
        return(final_list)


solution = Solution()
print(solution.kidsWithCandies(candies, extraCandies))