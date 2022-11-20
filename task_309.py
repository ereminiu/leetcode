from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = n * [0]
        ans = 0
        for i in range(n):
            if i > 0:
                dp[i] = dp[i-1]
            
            for j in range(i-1, -1, -1):
                if j > 1:
                    dp[i] = max(dp[i], prices[i]-prices[j] + dp[j-2])
                else:
                    dp[i] = max(dp[i], prices[i]-prices[j])

            ans = max(ans, dp[i])
        
        print(dp)
        return ans

print(Solution().maxProfit(prices=[6, 1, 6, 4, 3, 0, 2]))
print(Solution().maxProfit(prices=[1,2,3,0,2]))
print(Solution().maxProfit(prices=[1, 2]))