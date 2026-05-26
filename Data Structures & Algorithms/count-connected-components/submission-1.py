class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        
        for i in range(n):
            adj[i] = []
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for n in adj[node]:
                if n not in visited:
                    dfs(n)

        counter = 0
        for i in range(n):
            if i not in visited:
                counter += 1
                dfs(i)

        return counter