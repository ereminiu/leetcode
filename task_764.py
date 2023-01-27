from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        if len(mines) == n**2:
            return 0
        
        hor = [[0 for x in range(n)] for y in range(n)]
        ver = [[0 for x in range(n)] for y in range(n)]

        st_mines = set()
        for x, y in mines:
            st_mines.add((x, y))
        
        for i in range(n):
            for j in range(n):
                if (i, j) in st_mines:
                    hor[i][j] = 0
                    ver[i][j] = 0
                else:
                    hor[i][j] = (0 if j == 0 else hor[i][j-1]) + 1
                    ver[i][j] = (0 if i == 0 else ver[i-1][j]) + 1
        
        ans = 1
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) in st_mines:
                    hor[i][j] = 0
                    ver[i][j] = 0
                else:
                    hor[i][j] = min(hor[i][j], (0 if j == n-1 else hor[i][j+1]) + 1)
                    ver[i][j] = min(ver[i][j], (0 if i == n-1 else ver[i+1][j]) + 1)
                
                ans = max(ans, min(hor[i][j], ver[i][j]))
        
        return ans
        
print(Solution().orderOfLargestPlusSign(n = 5, mines = []))
print(Solution().orderOfLargestPlusSign(n = 5, mines = [[4,2]]))
print(Solution().orderOfLargestPlusSign(n = 1, mines = [[0,0]]))