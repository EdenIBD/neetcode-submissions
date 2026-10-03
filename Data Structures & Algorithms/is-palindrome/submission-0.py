class Solution:
    def isPalindrome(self, s: str) -> bool:
        inv = str()
        strip = str()
        for i in range(len(s)):
            if s[-(i+1)].isalnum():
                inv += s[-(i+1)]
            if s[i].isalnum():    
                strip += s[i]

        return inv.lower() == strip.lower()


        