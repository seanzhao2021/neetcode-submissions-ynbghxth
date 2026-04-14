class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #dfs search
        def dfs(x, y, grid):
            #base cases:
            #already visited this node (in set)
            # if (x, y) in visited:
            #     return
            #go past edges of board
            if (x < 0 or x >= len(grid)) or (y < 0 or y >= len(grid[0])):
                return
            #found water (0)
            if grid[x][y] == "0":
                return

            #add coord to set
            #visited.add(tuple([x, y]))
            grid[x][y] = "0"
            #dfs
            dfs(x + 1, y, grid)
            dfs(x - 1, y, grid)
            dfs(x, y + 1, grid)
            dfs(x, y - 1, grid)

        #visited = set()
        res = 0

        #when we find a 1 that is not visited, use dfs to explore that entire island and increment count
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                # if grid[x][y] == "1" and (x, y) not in visited:
                if grid[x][y] == "1":
                    dfs(x, y, grid)
                    res = res + 1
        
        return res

        
        