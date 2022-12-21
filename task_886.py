from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        gr = [[] for x in range(n)]
        for x, y in dislikes:
            gr[x-1].append(y-1)
            gr[y-1].append(x-1)
        
        can = True
        col = n * [-1]

        def dfs(x, c):
            col[x] = c
            for y in gr[x]:
                if col[y] == -1:
                    dfs(y, c^1)
                elif col[y] == c:
                    nonlocal can
                    can = False
                    return

        for i in range(n):
            if col[i] == -1:
                dfs(i, 0)
        
        return can

print(Solution().possibleBipartition(n = 4, dislikes = [[1,2],[1,3],[2,4]]))
print(Solution().possibleBipartition(n = 3, dislikes = [[1,2],[1,3],[2,3]]))
print(Solution().possibleBipartition(n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]))