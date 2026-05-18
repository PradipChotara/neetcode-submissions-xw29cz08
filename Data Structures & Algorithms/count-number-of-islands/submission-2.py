class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return
        
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        uf = UnionFind(row*col)

        islands = 0

        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    islands += 1

        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    current_id = r * col + c
                    for (dx,dy) in directions:
                        nr = r+dx
                        nc = c+dy
                        n_id = nr * col + nc
                        if 0<=nr<row and 0<=nc<col and grid[nr][nc] == '1':
                            if uf.union(current_id, n_id):
                                islands -= 1
        
        return islands
