from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        counter = 0
        visited = set()

        def bfs(node):
            q = deque()
            q.append(node)
            visited.add(node)

            while q:
                item = q.popleft()
                for n in adj[item]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)

        for i in range(n):
            if i not in visited:
                counter += 1
                bfs(i)
        
        return counter