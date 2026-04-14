class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            #base case 
                #i == len(s)
                #means we went through whole string exactly (no overshoot)
                #return 1
            if i == len(s):
                return 1
            
            #check if number we are decoding is 0
            #if trailing 0 or is equal to 0: fails
            if s[i] == "0":
                return 0

            res = dp(i + 1)

            memo[i+1] = res

            #there are at least two digits less and less than 26
            if i < len(s) - 1 and s[i:i+2] < "27":
                res += dp(i + 2)
            
            return res


        return dp(0)
 