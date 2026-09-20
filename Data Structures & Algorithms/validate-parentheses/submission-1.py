class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_set = {
            "{":"}",
            "(":")",
            "[":"]"
        }

        for c in s:
            if c in open_set:
                stack.append(c)
            else:
                if len(stack) <= 0 or open_set[stack[-1]] != c:
                    return False
                stack.pop()
        
        return len(stack)==0