from functools import cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = int(1e9+7)

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]

        def inside(x, y):
            return 0 <= x < m and 0 <= y < n

        @cache
        def solve(x, y, k):
            if k == 0:
                if x == startRow and y == startColumn:
                    return 1
                
                return 0
            
            ret = 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if inside(nx, ny):
                    ret += solve(nx, ny, k-1)
                    if ret >= MOD:
                        ret -= MOD
            
            return ret
    
        ans = 0
        for i in range(-1, m+1):
            for j in range(-1, n+1):
                if inside(i, j):
                    continue

                for k in range(0, maxMove+1):
                    ans += solve(i, j, k)
                    if ans >= MOD:
                        ans -= MOD
        
        return ans

print(Solution().findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0))
print(Solution().findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))