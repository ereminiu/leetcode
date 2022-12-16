from typing import List

class Solution:
    def mctFromLeafValues(self, a: List[int]) -> int:
        n = len(a)
        mx = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    mx[i][j] = a[i]
                    continue
                mx[i][j] = max(mx[i][j-1], a[j])
        dp = [[0 for x in range(n)] for y in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = a[i]
                    continue
                if i == j-1:
                    dp[i][j] = a[i] + a[j] + a[i] * a[j]
                    continue
                dp[i][j] = int(1e9+228)
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + mx[i][k]*mx[k+1][j])
        return dp[0][n-1] - sum(a)

print(Solution().mctFromLeafValues(a = [6,2,4]))