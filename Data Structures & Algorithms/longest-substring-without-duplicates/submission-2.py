class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #define l, r pointers at 0
        l, r = 0, 0
        #hashset init
        hs = set()
        #maximum val = 0
        maximum = 0

        #while r pointer does not touch end of string
        while r < len(s):
            #if string[r] is not in hashset
            if s[r] not in hs:
                #hashet.add string[r]
                hs.add(s[r])
                #if len hashset > maximum:
                    #set new maximum
                if len(hs) > maximum: maximum = len(hs) 
                #r increment by 1
                r += 1
            #else
            else:
                #hashset.remove string[l]
                hs.remove(s[l])
                #l increment by 1
                l += 1

        
        #return maximum
        return maximum