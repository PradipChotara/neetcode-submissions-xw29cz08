import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n+1)}
        for u,v,w in times:
            adj[u].append([v,w])

        dist = [float('inf')] * (n+1)
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            curr, u = heapq.heappop(pq)

            if curr > dist[u]:
                continue

            for v, weight in adj[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq,(dist[v], v))
        
        max_dist = 0
        for x in dist[1:]:
            if x == float('inf'):
                return -1
            max_dist = max(max_dist, x)
        
        return max_dist