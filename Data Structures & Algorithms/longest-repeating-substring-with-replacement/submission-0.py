class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def maxFreq(ht):
            temp = 0
            for key in ht:
                temp = max(ht[key], temp)
            return temp

        ht = {}
        res = 0

        #sliding window
        #every time right pointer moves, save letter to ht or increment its count
        l, r = 0, 0


        while r < len(s):
            if s[r] not in ht:
                ht[s[r]] = 1
            else:
                ht[s[r]] += 1
            #rule check is windows size - max freq >= k?
            while (r - l + 1) - maxFreq(ht) > k:
                ht[s[l]] -= 1
                l += 1

            #save max freq
            res = max(r - l + 1, res)
            r += 1

        return res
            
            



        