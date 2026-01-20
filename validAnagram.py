class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check length beforehand for optimization
        if len(s) != len(t):
            return False
        # hashMaps for holding key, value pairs of strings
        s_count = {}
        t_count = {}

        for letter in s:
            # loop the s string, and if letter in hashMap +1, unless equals to 1
            if letter in s_count:
                s_count[letter] += 1
            else:
                s_count[letter] = 1

        for letter in t:
            # loop the t string, and if letter in hashMap +1, unless equals to 1
            if letter in t_count:
                t_count[letter] += 1
            else:
                t_count[letter] = 1
        # checks the equalness of both hashMaps (k, v)
        return s_count == t_count
