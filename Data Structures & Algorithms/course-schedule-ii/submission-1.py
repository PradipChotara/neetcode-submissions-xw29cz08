from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        q = deque()
        for u,v in prerequisites:
            indegree[u] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        res = []

        while q:
            for _ in range(len(q)):
                item = q.popleft()
                for u,v in prerequisites:
                    if v == item:
                        indegree[u] -= 1
                        if indegree[u] == 0:
                            q.append(u)
                res.append(item)

        for i in range(len(indegree)):
            if indegree[i] != 0:
                return []
        
        return res     