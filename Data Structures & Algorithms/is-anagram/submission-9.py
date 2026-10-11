class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        letters = set()
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in dict_s:
                dict_s[letter] += 1
            else: 
                dict_s[letter] = 1

        for letter in t:
            if letter in dict_t:
                dict_t[letter] += 1
            else: 
                dict_t[letter] = 1
        
        for letter in s:
            try:
                if dict_s[letter] != dict_t[letter]:
                    return False
            except KeyError:
                return False

        return True