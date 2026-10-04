class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "[", "{"]
        stack = []
        inverted = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) != 0 and inverted[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0

