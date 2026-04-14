class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dpArr = [0] * n
        def dp(num):
            #base case
            if num == 1 or num == 2:
                return num
            if num < 1:
                return 0

            #f(n) = f(n-1) + f(n-2)
            #if a not in dp arr
            if dpArr[num - 1] == 0:
                #a = f(n-1)
                a = dp(num - 1)
                #add a to dpArr
                dpArr[num - 1] = a
            else:
                #get a from dpArr
                a = dpArr[num - 1]
            #b = f(n-2)
            if dpArr[num - 2] == 0:
                #a = f(n-1)
                b = dp(num - 2)
                #add a to dpArr
                dpArr[num - 2] = b
            else:
                #get a from dpArr
                b = dpArr[num - 2]

            return a + b
        x = dp(n)
        return x
