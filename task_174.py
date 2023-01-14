from typing import List

class Solution:
    def calculateMinimumHP(self, a: List[List[int]]) -> int:
        n, m = len(a), len(a[0])
        dp = [[0 for x in range(m)] for y in range(n)]

        dp[n-1][m-1] = max(1, 1-a[n-1][m-1])

        for i in range(n-2, -1, -1):
            dp[i][m-1] = max(1, dp[i+1][m-1] - a[i][m-1])
        
        for j in range(m-2, -1, -1):
            dp[n-1][j] = max(1, dp[n-1][j+1] - a[n-1][j])
        
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - a[i][j])

        return dp[0][0]

print(Solution().calculateMinimumHP(a = [[-2,-3,3],[-5,-10,1],[10,30,-5]]))
print(Solution().calculateMinimumHP(a = [[0]]))