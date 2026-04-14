class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """




        def lenPalindrome(s, l, r):
            #left and right in bounds
            #left and right equal to each other
            ans = ""
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                # print(l, r)
                # print(s[l: r+1])
                ans = s[l:r + 1]
                l -= 1
                r += 1
            
            return ans
        
        best = ""

        for i in range(len(s)):
            temp1 = lenPalindrome(s, i, i)
            temp2 = lenPalindrome(s, i, i + 1)

            if len(temp2) > len(temp1):
                best = temp2 if len(temp2) > len(best) else best
            else:
                best = temp1 if len(temp1) > len(best) else best
        
        return best

            