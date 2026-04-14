class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def volume(l, r, height):
            return min(height[r], height[l]) * (r - l)
        
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(volume(l, r, height), res)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res