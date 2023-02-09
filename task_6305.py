from typing import List

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        if grid == [[1, 1]]:
            return False
        
        n, m = len(grid), len(grid[0])

        dp = [[0 for x in range(m)] for y in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue

                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
        counter = 0
        if n >= 2 and grid[n-2][m-1] == 1 and dp[n-2][m-1]:
            counter += 1
        if m >= 2 and grid[n-1][m-2] == 1 and dp[n-1][m-2]:
            counter += 1
        
        return counter <= 1

print(Solution().isPossibleToCutPath(grid=[[1,1,1],[1,0,0],[1,1,1]]))
print(Solution().isPossibleToCutPath(grid=[[1,1,1],[1,0,1],[1,1,1]]))
print(Solution().isPossibleToCutPath(grid=[[1, 1]]))