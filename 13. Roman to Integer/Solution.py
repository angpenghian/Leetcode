s = "MCMXCIV"

class Solution:
    def romanToInt(self, s: str) -> int:
        total_sum = 0
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for charaters in s:
            value = roman_dict[charaters]
            total_sum += value
        return total_sum
        
solution = Solution()
print(solution.romanToInt(s))