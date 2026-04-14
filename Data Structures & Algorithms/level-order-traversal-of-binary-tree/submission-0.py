# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        queue = deque()
        if root is not None:
            queue.append(root)

        def bfs():
            if not queue:
                return

            temp = []
            
            for _ in range(len(queue)):
                #pop from queue
                curr = queue.popleft()
    
                #add that nodes left and right given that they are not null
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                #append to temp arr
                temp.append(curr.val)
            #append temp to res
            print(temp)
            res.append(temp)
            bfs()
        bfs()
        return res