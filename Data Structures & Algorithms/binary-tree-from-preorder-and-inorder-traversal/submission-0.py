# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        #divide and conquer
        #find left and right subtrees from root
        #root.left = left subtree and .right = right subtree
        #recursively build subtrees and roots

        #first element of inorder traversal is the root
        #traverse preorder until we find the root
            #everything to the left of that root in preorder is the left side of the tree
            #everything to the right is the right side of the tree
        #recursively build subtrees

        self.i = 0

        ht = {}
        for i in range(len(inorder)):
             ht[inorder[i]] = i

        def dac(l, r):
            #baes case
            if l > r:
                return None
            
            target = preorder[self.i]
            self.i += 1

            root = TreeNode(target)

            pos = ht[target]

            #left
            root.left = dac(l, pos - 1)
            #right
            root.right = dac (pos + 1, r)

            return root
        
        return dac(0, len(inorder) - 1)