class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        memo = {}
        def best(num):
            
            if num >= len(nums):
                return 0
            if num in memo:
                return memo[num]
            
            curr = nums[num] + best(num+2)
            next = best(num+1)

            memo[num] = max(curr, next)

            return memo[num]
        
        return best(0)