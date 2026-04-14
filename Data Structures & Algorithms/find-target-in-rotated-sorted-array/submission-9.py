class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #define pointers
        l, r = 0, len(nums) - 1

        #bin search
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid

            #check if left sorted segment:
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            #right sorted segment
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1




        return -1