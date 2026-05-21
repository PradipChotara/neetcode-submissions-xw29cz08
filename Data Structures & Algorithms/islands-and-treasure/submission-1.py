from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    q.append((x,y,1))
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        while q:
            x, y, lvl = q.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue
                if lvl < grid[nx][ny]:
                    grid[nx][ny] = lvl
                    q.append((nx, ny, lvl+1))  