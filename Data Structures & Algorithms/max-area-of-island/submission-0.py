class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(x,y):
            visited.add((x,y))
            count = 1
            for dx, dy in directions:
                nx = x+dx
                ny = y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1 and (nx,ny) not in visited:
                    count += dfs(nx,ny)
            return count

        max_islands = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and (x,y) not in visited:
                   max_islands = max(dfs(x,y), max_islands) 
        
        return max_islands