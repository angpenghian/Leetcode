from typing import List

chars = ["a","a","b","b","c","c","c"]

class Solution:
    def compress(self, chars: List[str]) -> int:
        dict = {}
        
        for alphabet in chars:
            if alphabet in dict:
                dict[alphabet] += 1
            else:
                dict[alphabet] = 1
                
        chars.clear()
        for key, value in dict.items():
            chars.append(key)
            chars.append(str(value))
            
        return (len(chars))
            
solution = Solution()
print(solution.compress(chars))