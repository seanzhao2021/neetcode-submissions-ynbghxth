class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []

        def backtrack(i, arr, total):
            if total == target:
                results.append(arr[:])
                return
                
            # for j in range(i, len(candidates)):
            #     if total + candidates[j] > target:
            #         return
            #     arr.append(candidates[j])
            #     backtrack(j, arr, total + candidates[j])
            #     arr.pop()

            if i >= len(candidates) or total > target:
                return

            arr.append(candidates[i])
            backtrack(i, arr, total + candidates[i])
            arr.pop()
            backtrack(i + 1, arr, total)
                
        backtrack(0,[],0)
        return results

