class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.globalMax = nums[0]
        self.minProduct = nums[0]
        self.maxProduct = nums[0]

        for i in range(1, len(nums)):
            extendMax = self.maxProduct * nums[i]
            extendMin = self.minProduct * nums[i]

            self.maxProduct = max(extendMax, extendMin, nums[i])
            self.minProduct = min(extendMax, extendMin, nums[i])

            self.globalMax = max(self.globalMax, self.maxProduct)
        
        return self.globalMax