from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows  = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def bfs(x,y):
            q = deque()
            q.append((x,y))
            visited.add((x,y))
            area = 1
            while q:
                x,y = q.popleft()
                for dx, dy in directions:
                    nx = x+dx
                    ny = y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1 and (nx,ny) not in visited:
                        q.append((nx,ny))
                        visited.add((nx,ny))
                        area += 1
            return area

        max_island = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and (x,y) not in visited:
                    max_island = max(max_island, bfs(x,y))
        return max_island