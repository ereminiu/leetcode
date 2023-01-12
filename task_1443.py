from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.ans = 0
        self.apples = n * [0]
        
        def go(u, par):
            if hasApple[u]:
                self.apples[u] = 1
            
            for v in gr[u]:
                if v != par:
                    self.apples[u] += go(v, u)
            
            return self.apples[u]
        
        def dfs(u, par):
            if not self.apples[u]:
                return
            
            for v in gr[u]:
                if self.apples[v] and v != par:
                    self.ans += 1
                    dfs(v, u)
        
        gr = [[] for x in range(n)]
        for x, y in edges:
            gr[x].append(y)
            gr[y].append(x)
        
        go(0, -1)
        dfs(0, -1)

        return 2 * self.ans

print(Solution().minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]))
print(Solution().minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))