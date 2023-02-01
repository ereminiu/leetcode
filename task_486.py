from functools import cache
from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        pref = n * [0]
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + nums[i]
        
        def get_sum(l, r):
            return pref[r] if l == 0 else pref[r] - pref[l-1]
        
        dp = [[-1 for x in range(n)] for j in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                    continue

                dp[i][j] = max(nums[i] + get_sum(i+1, j) - dp[i+1][j], nums[j] + get_sum(i, j-1) - dp[i][j-1])
        
        return 2 * dp[0][n-1] >= pref[-1]

print(Solution().PredictTheWinner(nums = [1,5,2]))
print(Solution().PredictTheWinner(nums = [1,5,233,7]))