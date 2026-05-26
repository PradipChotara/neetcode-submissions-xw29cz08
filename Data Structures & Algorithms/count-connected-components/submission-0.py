class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:    
        visited = set()

        def dfs(node):
            visited.add(node)
            
            for u,v in edges:
                if u == node and v not in visited:
                    dfs(v)
                if v == node and u not in visited:
                    dfs(u)

        counter = 0
        for i in range(n):
            if i not in visited:
                counter += 1
                dfs(i)

        return counter