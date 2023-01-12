from typing import List
from collections import deque
from collections import Counter

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, max_k: int) -> int:
        inf = int(1e9+228)
        dp = [[inf for x in range(max_k+1)] for y in range(n)]

        for x, y, s in flights:
            if x == src:
                dp[y][0] = s
        
        dp[src][0] = 0
        for k in range(1, max_k+1):
            for i in range(n):
                dp[i][k] = dp[i][k-1]
            
            for u, v, s in flights:
                dp[v][k] = min(dp[v][k], dp[u][k-1] + s)
        
        ans = dp[dst][max_k]
        return -1 if ans == inf else ans

print(Solution().findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, max_k = 1))
print(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, max_k = 1))
print(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, max_k = 0))