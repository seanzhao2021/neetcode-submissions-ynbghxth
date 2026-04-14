class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #define house robber prob
        memo_a = {}
        memo_b = {}
        def dfs(i, arr, memo):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]
            
            curr = arr[i] + dfs(i + 2, arr, memo)
            next = dfs(i + 1, arr, memo)
            
            memo[i] = max(curr,next)
            return memo[i]

        n = len(nums)

        if len(nums) == 1:
            return nums[0]

        return max(dfs(0, nums[0:n-1], memo_a), dfs(0, nums[1:n], memo_b))