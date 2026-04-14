class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for element in nums:
            if element in hs:
                return True
            else: hs.add(element)
        return False