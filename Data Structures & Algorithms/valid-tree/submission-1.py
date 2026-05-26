from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i : [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def bfs(node, parent):
            q = deque()
            q.append((node, parent))
            visited.add(node)

            while q:
                node, parent = q.popleft()
                for n in adj[node]:
                    if n == parent:
                        continue
                    if n in visited:
                        return False
                    q.append((n, node))
                    visited.add(n)
            return True

        return bfs(0,-1) and len(visited) == n
