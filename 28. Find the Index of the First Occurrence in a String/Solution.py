haystack = "hello"
needle = "ll"

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start_index = 0
        end_index = len(needle)
        hold_index = []
        for i in range(len(haystack)):
            check = haystack[start_index:end_index]
            if check == needle:
                hold_index.append(start_index)
                
            start_index += 1
            end_index += 1
            
        return hold_index[0] if hold_index else -1
        
        
solution = Solution()
print(solution.strStr(haystack, needle))