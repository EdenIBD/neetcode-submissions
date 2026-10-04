class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        stack = []
        inverted = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        iter = 0
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) != 0 and inverted[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0

