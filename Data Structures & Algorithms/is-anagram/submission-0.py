class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ht_s = {}
        ht_t = {}

        for i in range (len(s)):
            if not s[i] in ht_s: 
                ht_s.update({s[i] : 1})
            else:
                ht_s[s[i]] += 1



            if not t[i] in ht_t: 
                ht_t.update({t[i] : 1})
            else:
                ht_t[t[i]] += 1

        return ht_s == ht_t