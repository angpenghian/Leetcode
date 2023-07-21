from typing import List

strs = ["eat","tea","tan","ate","nat","bat"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word] = [word]
                
        return list(groups.values())
            
        
solution = Solution()
print(solution.groupAnagrams(strs))