class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        dp = (n+1) * [int(1e9+227)]

        for i in range(1, n+1):
            dp[i] = min(dp[i], i)
            for k in range(2, 1000):
                if k*i > n:
                    break
                dp[k*i] = min(dp[k*i], dp[i] + k)
        
        return dp[n]

print(Solution().minSteps(3))
print(Solution().minSteps(1))
print(Solution().minSteps(2))
print(Solution().minSteps(9))