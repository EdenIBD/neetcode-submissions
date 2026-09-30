class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        letters = set()
        for letter in s:
            countS[letter] = 0
            letters.add(letter)
        for letter in s: 
            countS[letter] += 1

        for letter in t:
            countT[letter] = 0
        for letter in t: 
            countT[letter] += 1

        for letter in letters:
            try:
                if countS[letter] != countT[letter]:
                    return False
            except KeyError:
                return False

        return True

        


        