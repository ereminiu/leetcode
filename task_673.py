from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = n * [0]
        amount = n * [0]

        mx, ans = 0, 0
        for i in range(n):
            dp[i] = 1
            amount[i] = 1
            for j in range(0, i):
                if nums[i] <= nums[j]:
                    continue
                if dp[j] >= dp[i]:
                    dp[i] = dp[j]+1
                    amount[i] = amount[j]
                elif dp[j] == dp[i]-1:
                    amount[i] += amount[j]
            
            if dp[i] == mx:
                ans += amount[i]
            elif dp[i] > mx:
                ans = amount[i]
                mx = dp[i]
        
        return ans

print(Solution().findNumberOfLIS(nums = [1,3,5,4,7]))
print(Solution().findNumberOfLIS(nums = [2,2,2,2,2]))
print(Solution().findNumberOfLIS(nums = [1,2,4,3,5,4,7,2]))