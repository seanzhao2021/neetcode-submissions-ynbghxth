class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort array
        nums.sort()

        hs = set()

        #for i, element in enumerate(nums) 
        for i, element in enumerate(nums):
            #set l, r pointers (to the right of current element)
            l, r = i + 1, len(nums) - 1


            #while (l < r)
            while(l < r):
                #target = element * -1
                target = element * -1
                sum = nums[l] + nums[r]

                #if nums[l] + nums[r] == target
                if sum == target:
                    #append result to sol arr
                    #use hashet to detect dupes
                    hs.add(tuple([element, nums[l], nums[r]]))
                    #move both pointers
                    l, r = l + 1, r - 1
                #if pointer sum less than target
                elif sum < target:
                    #move left pointer to the right
                    l += 1
                #else
                else:
                    #move right pointer to the left
                    r -= 1
        #reutrn array
        return list(hs)