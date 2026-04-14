class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        rs = 0
        curr = 0
        ans = nums[0]

        for i in range (len(nums)):
            curr = nums[i]
            rs = rs + curr

            if curr > rs:
                rs = curr
            
            ans = max(ans, rs)
        

        return ans