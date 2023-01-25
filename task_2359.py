from typing import List
from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        gr = [[] for x in range(n)]
        for i in range(n):
            if edges[i] != -1:
                gr[i].append(edges[i])

        inf = int(1e9+228)
        
        def get_dist(st):
            q = deque()
            q.append(st)
            dist = n * [inf]
            dist[st] = 0

            while q:
                u = q.pop()
                for v in gr[u]:
                    if dist[v] > dist[u] + 1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            
            return dist

        from_a = get_dist(node1)
        from_b = get_dist(node2)

        # print(f'from_a = {from_a}')
        # print(f'from_b = {from_b}')
        
        idx, val = -1, inf
        for i in range(n):
            if from_a[i] != inf and from_b[i] != inf:
                if val > max(from_a[i], from_b[i]):
                    val = max(from_a[i], from_b[i])
                    idx = i

        return idx

print(Solution().closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
print(Solution().closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2))