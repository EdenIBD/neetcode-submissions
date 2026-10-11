class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        for char in s:
            if not char.isalnum():
                s = s.replace(char, "")
        
        inverted = []
        for i in range(len(s)):
            inverted.append(s[-1-i])

        s = list(s)
        
        return s == inverted