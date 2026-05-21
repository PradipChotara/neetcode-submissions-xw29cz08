from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        for u,v in prerequisites:
            indegree[u] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        if len(q) <= 0:
            return False

        while q:
            item = q.popleft()
            for u,v in prerequisites:
                if item != v:
                    continue
                indegree[u] -= 1
                if indegree[u] == 0:
                    q.append(u)

        for i in range(len(indegree)):
            if indegree[i] != 0:
                return False

        return True