from typing import List
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        mx = max(nums)
        
        dp = Counter()
        dp[0] = 0
        for x in range(1, mx+1):
            dp[x] = max(dp[x-1], counter[x] * x + dp[x-2])
        return dp[mx]

print(Solution().deleteAndEarn(nums=[3,4,2]))
print(Solution().deleteAndEarn(nums=[2,2,3,3,3,4]))
print(Solution().deleteAndEarn(nums=[1,1,1,2,4,5,5,5,6]))