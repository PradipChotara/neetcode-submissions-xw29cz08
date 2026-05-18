from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        row = len(grid)
        col = len(grid[0])
        
        def bfs(x,y):
            visited.add((x,y))
            q = deque()
            q.append((x,y))
            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            while q:
                (x,y) = q.popleft()
                for (dx,dy) in directions:
                    nx = x+dx
                    ny = y+dy
                    if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited and grid[nx][ny] == '1':
                        q.append((nx,ny))
                        visited.add((nx,ny))
        
        count = 0
        for x in range(row):
            for y in range(col):
                if (x,y) not in visited and grid[x][y] == '1':
                    bfs(x,y)
                    count += 1
        return count
