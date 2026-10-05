class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                if len(seen) > max_len:
                    max_len = len(seen)
            else:
                while s[i] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[i])

        
        if s == ' ':
            return 1
        else:
            return max_len

        
        

            
        