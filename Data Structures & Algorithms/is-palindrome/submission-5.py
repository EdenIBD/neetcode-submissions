class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '').lower()
        og = []
        inv = []
        for char in s:
            if char.isalnum() == True:
                og.append(char)
        
        for i in range(1, len(og)+1):
            inv.append(og[-i])
        
        return og == inv

        