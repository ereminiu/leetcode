from typing import List

class Solution:
    def allPathsSourceTarget(self, gr: List[List[int]]) -> List[List[int]]:
        n = len(gr)
        par = [[] for x in range(n)]
        used = n * [False]

        def dfs(u, prev):
            used[u] = True
            for v in gr[u]:
                par[v].append(u)
                if not used[v]:
                    dfs(v, u)
        
        dfs(0, -1)

        ans = []
        
        def go(a, path):
            if a == 0:
                ans.append(path[::-1] + [n-1])
                # path.pop()
                return
            for x in par[a]:
                path.append(x)
                go(x, path)
                path.pop()
        
        for a in par[n-1]:
            go(a, [a])
        
        return ans

print(Solution().allPathsSourceTarget(gr = [[1,2],[3],[3],[]]))
print(Solution().allPathsSourceTarget(gr = [[4,3,1],[3,2,4],[3],[4],[]]))