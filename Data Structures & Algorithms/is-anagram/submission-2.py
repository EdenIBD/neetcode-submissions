class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        letters = set()
        for letter in s:
            if letter in countS:
                countS[letter] += 1
            else:
                countS[letter] = 1
            letters.add(letter)

        for letter in t:
            if letter in countT:
                countT[letter] += 1
            else:
                countT[letter] = 1

        return countS == countT

        


        