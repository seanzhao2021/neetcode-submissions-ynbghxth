class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #define pointers
        l, r = 0, len(nums) - 1

        # #while left does not cross right
        # while l <= r:
        #     #define midpoint
        #     mid = (l + r) // 2
        #     print(l , r, mid)
        #     #if mid is target
        #     if nums[mid] == target:
        #         #return mid
        #         return mid

        #     if nums[l] == target: return l
        #     if nums[r] == target: return r

        #     #if left < target < mid
        #     if nums[l] < target and target < nums[mid]:
        #         #move right pointer down
        #         r = mid - 1
        #     #else move left pointer up
        #     else: l = mid + 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid

            if nums[l] == target: return l
            if nums[r] == target: return r

            if nums[l] < nums[mid]:
                #left side is ordered
                if nums[l] < target and target < nums[mid]:
                    r = mid - 1
                else: l = mid + 1
            else:
                #right side is ordered
                if nums[r] > target and target > nums[mid]:
                    l = mid + 1
                else: r = mid - 1
        
        #return -1
        return -1