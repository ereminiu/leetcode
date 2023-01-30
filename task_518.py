from typing import List
from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = (amount + 1) * [0]
        dp[0] = 1
        for c in coins:
            for x in range(c, amount+1):
                dp[x] += dp[x-c]
        
        return dp[amount]
        
print(Solution().change(amount = 5, coins = [1,2,5]))
print(Solution().change(amount = 3, coins = [2]))
print(Solution().change(amount = 10, coins = [10]))