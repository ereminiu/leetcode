from typing import List
from collections import Counter

class Dsu:
    def __init__(self, N: int):
        self.N = N
        self.par = [i for i in range(N)]
        self.rank = N * [0]
    
    def get_par(self, x: int) -> int:
        if x != self.par[x]:
            self.par[x] = self.get_par(self.par[x])
        return self.par[x]
    
    def same(self, x: int, y: int) -> bool:
        return self.get_par(x) == self.get_par(y)
    
    def merge(self, x: int, y: int) -> None:
        x, y = self.get_par(x), self.get_par(y)

        if x == y:
            return
        
        if x < y:
            self.par[y] = x
        else:
            self.par[x] = y

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        gr = [[] for x in range(n)]
        for u, v in edges:
            gr[u].append(v)
            gr[v].append(u)
        
        all = {}
        for i in range(n):
            if vals[i] not in all:
                all[vals[i]] = []

            all[vals[i]].append(i)

        print(gr)
        
        ufo = Dsu(n)
        ans = 0

        for e in all:
            nodes = all[e]

            # print(f'nodes = {nodes}')

            for u in nodes:
                for v in gr[u]:
                    if vals[u] >= vals[v]:
                        # print(u, v)
                        ufo.merge(u, v)
            
            counter = Counter()
            for u in nodes:
                if ufo.get_par(u) not in counter:
                    counter[ufo.get_par(u)] = 1
                else:
                    counter[ufo.get_par(u)] += 1
                # print(ufo.get_par(u))
            
            print(counter)
            
            for x in counter:
                print(x, counter[x])
                print(counter[x])
                ans += (counter[x] * (counter[x] + 1) // 2)
            
        return ans

print(Solution().numberOfGoodPaths(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]))
# print(Solution().numberOfGoodPaths(vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]))
# print(Solution().numberOfGoodPaths(vals = [1], edges = []))