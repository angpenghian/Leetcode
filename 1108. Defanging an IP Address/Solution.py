address = "1.1.1.1"

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return(address.replace(".", "[.]"))
        
solution = Solution()
print(solution.defangIPaddr(address))