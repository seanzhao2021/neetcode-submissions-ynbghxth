class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #iterate through array adding to hashtable # of occurences
        #O(n) time
        ht = {}
        for element in nums:
            if element in ht:
                ht[element] += 1
            else:
                ht[element] = 1
        
        bucket = [[] for _ in range (len(nums))]

        for key in ht:
            bucket[ht[key] - 1].append(key)

        res= []

        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
                k = k - len(bucket[i])
            if k == 0:
                return res
        
        return res