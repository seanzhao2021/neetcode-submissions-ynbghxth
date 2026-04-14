class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        #create pacific 
        #create atlantic 
        pacific, atlantic = set(), set()

        def dfs(i, j, heights, visited, prev):
            #base cases
            #in bounds
            #not visited yet
            #heights of neighbor >= current height
            if (i < 0 or i >= len(heights)) or (j < 0 or j >= len(heights[0])):               
                return
            if tuple([i, j]) in visited:        
                return
            if heights[i][j] < prev:
                return
            

            visited.add(tuple([i, j]))

            dfs(i + 1, j, heights, visited, heights[i][j])
            dfs(i - 1, j, heights, visited, heights[i][j])
            dfs(i, j + 1, heights, visited, heights[i][j])
            dfs(i, j - 1, heights, visited, heights[i][j])
        
        for i in range(len(heights)):
            dfs(i, 0, heights, pacific, 0)
            dfs(i, len(heights[0]) - 1, heights, atlantic, 0)

        for j in range(len(heights[0])):
            dfs(0, j, heights, pacific, 0)
            dfs(len(heights) - 1, j, heights, atlantic, 0)

        res = []
        
        for tup in pacific:    
            if tup in atlantic:
                res.append(tup)
        
        return res