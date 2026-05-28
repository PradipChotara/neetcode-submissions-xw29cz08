import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst_cost = 0
        visited = set()

        minHeap = [(0,0)]
        
        while minHeap:
            w, u = heapq.heappop(minHeap)

            if u in visited:
                continue
            
            visited.add(u)

            mst_cost += w

            for i in range(len(points)):
                if i == u:
                    continue
                xi, yi = points[u]
                xj, yj = points[i]
                dist = abs(xi-xj) + abs(yi-yj)

                if i not in visited:
                    heapq.heappush(minHeap,(dist,i))
            
        return mst_cost