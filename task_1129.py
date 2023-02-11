from typing import List
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        gr_red, gr_blue = [[] for x in range(n)], [[] for x in range(n)]
        for u, v in redEdges:
            gr_red[u].append(v)
        
        for u, v in blueEdges:
            gr_blue[u].append(v)
        
        inf = int(1e9+228)
        from_red = n * [inf]
        from_blue = n * [inf]

        from_red[0], from_blue[0] = 0, 0
        q = deque()
        q.append(0)

        while q:
            u = q.pop()
            for v in gr_blue[u]:
                if from_blue[v] > from_red[u] + 1:
                    from_blue[v] = from_red[u] + 1
                    q.append(v)
            
            for v in gr_red[u]:
                if from_red[v] > from_blue[u] + 1:
                    from_red[v] = from_blue[u] + 1
                    q.append(v)
        
        ans = n * [-1]
        for i in range(n):
            ans[i] = min(from_red[i], from_blue[i])
            
            if ans[i] == inf:
                ans[i] = -1
        
        return ans

print(Solution().shortestAlternatingPaths(n = 3, redEdges = [[0,1],[1,2]], blueEdges = []))
print(Solution().shortestAlternatingPaths(n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]))