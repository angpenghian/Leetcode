from typing import List

arr = [1,2,2,1,1,3]

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence_dict = {}

        for number in arr:
            if number in occurrence_dict:
                occurrence_dict[number] += 1
            else:
                occurrence_dict[number] = 1

        unique_occurrence_set = set(occurrence_dict.values())
        
        if len(unique_occurrence_set) == len(occurrence_dict):
            return True
        else:
            return False

        
solution = Solution()
print(solution.uniqueOccurrences(arr))