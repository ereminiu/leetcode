from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        
        n, MX = len(nums), sum(nums)+1
        dp = [[False for x in range(MX)] for y in range(n+1)]
        dp[0][0] = True
        
        for i in range(1, n+1):
            for s in range(MX):
                dp[i][s] = dp[i-1][s-nums[i-1]] | dp[i-1][s]
            if dp[i][target]:
                return True
        
        return False