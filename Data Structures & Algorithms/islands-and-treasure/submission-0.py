class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x,y,lvl):

            if x < 0 or x >= rows or y < 0 or y >= cols:
                return
            
            if grid[x][y] == -1:
                return
            
            if lvl > grid[x][y]:
                return
            
            if grid[x][y] != 0:
                grid[x][y] = lvl
            
            dfs(x-1, y, lvl+1)
            dfs(x+1, y, lvl+1)
            dfs(x, y-1, lvl+1)
            dfs(x, y+1, lvl+1)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    dfs(x,y,0)