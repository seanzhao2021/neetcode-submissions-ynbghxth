# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        
        def dfs(root):
            if not root:
                return None

            #if p is less than or equal to root and q is greater than or equal to root then that node is the lowest descendent
            if p.val <= root.val and q.val >= root.val:
                return root
            elif q.val <= root.val and p.val >= root.val:
                return root
            
            if p.val < root.val:
                left = dfs(root.left)
                return left
            if p.val > root.val:
                right = dfs(root.right)
                return right
            

            # if not left and right: return right
            # if not right and left: return left

        
        
        return dfs(root)

