from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh_fruit = 0

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    q.append((x,y))
                if grid[x][y] == 1:
                    fresh_fruit += 1
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        counter = 0

        while q:
            flag = False
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx<0 or nx>=rows or ny<0 or ny>=cols or grid[nx][ny] == 2 or grid[nx][ny] == 0:
                        continue
                    q.append((nx,ny))
                    grid[nx][ny] = 2
                    fresh_fruit -= 1
                    flag = True
            if flag:
                counter += 1

        if fresh_fruit != 0:
            return -1
        
        return counter 