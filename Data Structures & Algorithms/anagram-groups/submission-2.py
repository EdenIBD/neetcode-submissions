class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def letter_dict(s):
            unique = set()
            for c in s:
                unique.add(c)

            l_dict = {}

            for c in s:
                if c in l_dict:
                    l_dict[c] += 1
                else:
                    l_dict[c] = 1

            return l_dict


        def matching(s1, s2):
            if len(s1) != len(s2):
                return False

            for c in letter_dict(s1):
                try:
                    if letter_dict(s1)[c] != letter_dict(s2)[c]:
                        return False
                except KeyError:
                    return False

            return True
    

        def main():
            groups = {}

            for word in strs:
                signature = ''.join(sorted(word))

                if signature in groups:
                    groups[signature].append(word)
                else:
                    groups[signature] = [word]
            
            return list(groups.values())
            

        return main()
                

        