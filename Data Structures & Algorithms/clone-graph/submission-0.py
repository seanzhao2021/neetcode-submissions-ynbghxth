"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        #baes case empty adj list
        if not node:
            return node

        ht = {}
        #dfs
        def dfs(node):
            #base case 
            #did we already clone this
            if node.val in ht:
                #return the clone
                return ht[node.val]
            
            #make clone of node
            copy = Node(node.val)
            ht[node.val] = copy

            #for each neighbor in the neighbor list
            for neighbor in node.neighbors:
                #get cloned neighbor from dfs
                copy_neighbor = dfs(neighbor)
                #append to clone.neighbors
                copy.neighbors.append(copy_neighbor)
            
            #return clone
            return copy

        return dfs(node)

        