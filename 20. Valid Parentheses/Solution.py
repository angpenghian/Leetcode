s = "()[]{"

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        # Convert string to a list because strings are immutable
        bracket_list = list(s)
        index = 0
        while index < len(bracket_list) - 1:
            current_bracket = bracket_list[index]
            corresponding_closing_bracket = bracket_pairs.get(current_bracket)
            
            # If the next bracket in the list is the corresponding closing bracket of the current bracket
            if bracket_list[index + 1] == corresponding_closing_bracket:
                # Remove both brackets from the list
                bracket_list.pop(index + 1)
                bracket_list.pop(index)
                
                # Step back one index to check for new valid pairs formed, if possible
                if index > 0:
                    index -= 1
            else:
                index += 1

        # If all brackets were correctly matched, the list will be empty
        return len(bracket_list) == 0
        
solution = Solution()
print(solution.isValid(s))