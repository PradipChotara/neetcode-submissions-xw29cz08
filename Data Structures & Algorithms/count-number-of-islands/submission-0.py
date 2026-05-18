class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        row = len(grid)
        col = len(grid[0])

        def dfs(x,y):
            visited.add((x,y))
            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            for (dx, dy) in directions:
                nx = x+dx
                ny = y+dy

                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == '1' and (nx,ny) not in visited:
                    dfs(nx, ny)

        count = 0

        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1' and (x,y) not in visited:
                    dfs(x,y)
                    count += 1
        
        return count