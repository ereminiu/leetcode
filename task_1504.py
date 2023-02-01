from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        pref = [[0 for x in range(m)] for y in range(n)]
        points = []
        
        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    points.append([i, j])
                
                pref[i][j] = mat[i][j]
                
                if i > 0:
                    pref[i][j] += pref[i-1][j]
                if j > 0:
                    pref[i][j] += pref[i][j-1]
                if i > 0 and j > 0:
                    pref[i][j] -= pref[i-1][j-1]
                
        def get_pref(rowL, colL, rowR, colR):
            ret = pref[rowR][colR]

            if colL > 0:
                ret -= pref[rowR][colL-1]
            if rowL > 0:
                ret -= pref[rowL-1][colR]
            if colL > 0 and rowL > 0:
                ret += pref[rowL-1][colL-1]
            
            return ret
        
        ans = 0
        for i, j in points:
            if not mat[i][j]:
                continue

            for x in range(i, n):
                for y in range(j, m):
                    if get_pref(i, j, x, y) == (x-i+1) * (y-j+1):
                        ans += 1
                    else:
                        break
        
        return ans

print(Solution().numSubmat(mat = [[1,0,1],[1,1,0],[1,1,0]]))
print(Solution().numSubmat(mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]))