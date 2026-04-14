class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #set pointers l = 0 and r = 0
        #set global max var
        l, r = 0, 0
        maxVal = 0

        #while r is not at the end
        while r < len(prices):
            #if l and r touching move r up by 1
            print(l, r)
            if l == r:
                r += 1

            #if r is smaller than l
                #move l to r
            elif prices[r] < prices[l]:
                l = r
            
            #if r - l greater than max
                #set max to r - 1
            elif prices[r] - prices[l] > maxVal:
                
                maxVal = prices[r] - prices[l]
            else:
                r += 1
            #r += 1

        #return argmax(max, 0)
        return max(maxVal, 0)