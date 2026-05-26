class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        total_nodes = set()
        for u,v in edges:
            total_nodes.add(u)
            total_nodes.add(v)

        uf = UnionFind(len(total_nodes))

        for u, v in edges:
            if not uf.union(u,v):
                return [u,v]
        