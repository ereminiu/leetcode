from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        inf = int(1e9+228)

        dp = (n+1) * [0]
        best_sell = (n+1) * [-inf]

        for i in range(1, n+1):
            price = prices[i-1]
            profit = price + best_sell[i-1]
            dp[i] = max(dp[i-1], profit)
            sold = -price - fee + dp[i-1]
            best_sell[i] = max(best_sell[i-1], sold)
        
        return dp[-1]

print(Solution().maxProfit(prices = [1,3,2,8,4,9], fee = 2))
print(Solution().maxProfit(prices = [1,3,7,5,10,3], fee = 3))