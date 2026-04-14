# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(root, lower, upper):
            #violate bst contraints
            #node is none
            #val is not less than upper or not greater than lower
            if root is None:
                return True

            if not (root.val < upper) or not (root.val > lower):
                return False

            #want to go left
            #check if left val is less than upper limit and bigger than lower limit
            #set val to new upper limit
            #go left

            #want to go right
            #check if right val is geater than lower limit and less than upper limit
            #set val to new lower limit
            #go right

            return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)

        return dfs(root, float('-inf'), float('inf'))
            