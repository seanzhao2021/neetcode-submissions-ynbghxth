class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ht = {}

        for i in range (len(nums)):
            x = target - nums[i]
            if x in ht:
                return [ht[x], i]
            else:
                ht.update({nums[i] : i})
        return[0, 0]