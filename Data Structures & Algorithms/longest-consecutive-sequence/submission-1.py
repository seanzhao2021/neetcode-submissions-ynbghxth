class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()

        for element in nums:
            hashSet.add(element)

        ans = 0

        for num in hashSet:
            if num - 1 in hashSet:
                continue
            else:
                temp = num
                length = 0
                while temp in hashSet:
                    length += 1
                    temp += 1
                ans = max(ans, length)
        
        return ans