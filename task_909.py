from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        next = (n*n+1) * [0]
        grid = [[0 for x in range(n)] for y in range(n)]

        val, count = 0, 0
        for i in range(n-1, -1, -1):
            for j in range(n):
                val += 1
                grid[i][j] = val
            if count % 2:
                grid[i] = grid[i][::-1]
            count += 1

            for j in range(n):
                next[grid[i][j]] = board[i][j]
        
        inf = int(1e9+228)
        dist = (n*n+1) * [inf]
        dist[1] = 0
        q = deque()
        q.append(1)
        while q:
            u = q.pop()
            for v in range(u+1, min(u+6, n*n)+1):
                to_go = v if next[v] == -1 else next[v]
                if dist[to_go] > dist[u] + 1:
                    dist[to_go] = dist[u] + 1
                    q.append(to_go)
        
        return -1 if dist[n*n] == inf else dist[n*n]

print(Solution().snakesAndLadders(board=[[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]))
print(Solution().snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(Solution().snakesAndLadders(board = [[-1,-1],[-1,3]]))