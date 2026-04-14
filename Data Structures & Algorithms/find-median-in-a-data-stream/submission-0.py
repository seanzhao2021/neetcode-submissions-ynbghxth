import heapq
class MedianFinder(object):

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.left:
            heapq.heappush(self.left, -1 * num)
        elif -1 * num >= self.left[0]:
            heapq.heappush(self.left, -1 * num)
        else:
            heapq.heappush(self.right, num)

        #left heap too big
        if len(self.left) - len(self.right) > 1:
            temp = heapq.heappop(self.left)
            heapq.heappush(self.right, -1 * temp)
        #right heap too big
        elif len(self.right) - len(self.left) > 1:
            temp = heapq.heappop(self.right)
            heapq.heappush(self.left, -1 * temp)

        #print(self.left, self.right)
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) == len(self.right):
            l, r = -1 * self.left[0], self.right[0]
            return (l + r) / 2.0
        elif len(self.left) > len(self.right):
            return -1 * self.left[0]
        else:
            return self.right[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()