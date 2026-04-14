class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # memo = {}
        # def best(num):
            
        #     if num >= len(nums):
        #         return 0
        #     if num in memo:
        #         return memo[num]
            
        #     curr = nums[num] + best(num+2)
        #     next = best(num+1)

        #     memo[num] = max(curr, next)

        #     return memo[num]
        
        # return best(0)


        memo = {}
        def dfs(i, arr, memo):
            if i >= len(arr):
                return 0
            
            if i in memo:
                return memo[i]
            else:
                curr = arr[i] + dfs(i + 2, arr, memo)
                next = dfs(i + 1, arr, memo)
            
            memo[i] = max(curr,next)
            return memo[i]

        return dfs(0, nums, memo)