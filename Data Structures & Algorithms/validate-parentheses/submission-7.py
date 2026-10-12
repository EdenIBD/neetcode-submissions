class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        inverted = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        for char in s:
            if char in inverted:
                stack.append(char)
            else:
                try:
                    if inverted[stack.pop()] != char:
                        return False
                    else:
                        continue
                except IndexError:
                    return False

        return len(stack) == 0
        