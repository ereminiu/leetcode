from collections import deque

class Solution:
    def numBusesToDestination(self, route, source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(route)
        sets = [set(route[i]) for i in range(n)]
        gr = [[] for x in range(n)]
        begin, end = [], []
        for i in range(n):
            for j in range(n):
                if i != j and len(sets[i]&sets[j]):
                    gr[i].append(j)
                if source in sets[i]:
                    begin.append(i)
                if target in sets[i]:
                    end.append(i)
        if set(begin) & set(end): # Это похоже на костыль, но это очень существенное отсечение
            return 1
        # print(gr)
        inf = int(1e9+228)
        ans = inf
        for x in begin:
            q = deque()
            q.append(x)
            dist = n * [inf]
            dist[x] = 1
            while q:
                u = q.pop()
                for v in gr[u]:
                    if dist[v] > dist[u]+1:
                        dist[v] = dist[u]+1
                        q.append(v)
            for y in end:
                ans = min(ans, dist[y])
        
        return -1 if ans == inf else ans

print(Solution().numBusesToDestination(route = [[1,2,7],[3,6,7]], source = 1, target = 6))