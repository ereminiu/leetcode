from typing import List
from collections import Counter

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.cnt = [Counter() for x in range(n)]
        self.ans = n * [0]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        def dfs(u, par):
            self.cnt[u][labels[u]] = 1
            for v in gr[u]:
                if v != par:
                    dfs(v, u)
                    for c in alphabet:
                        self.cnt[u][c] += self.cnt[v][c]
            self.ans[u] = self.cnt[u][labels[u]]

        gr = [[] for x in range(n)]
        for x, y in edges:
            gr[x].append(y)
            gr[y].append(x)
        
        dfs(0, -1)
        
        return self.ans

print(Solution().countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"))
print(Solution().countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"))
print(Solution().countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"))