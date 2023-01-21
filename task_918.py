from typing import List

class Solution:
    def maxSubarraySumCircular(self, a: List[int]) -> int:
        n = len(a)
        right_max = n * [0]
        right_max[n-1] = a[n-1]
        suff = a[n-1]
        for i in range(n-2, -1, -1):
            suff += a[i]
            right_max[i] = max(right_max[i+1], suff)
        
        dp = n * [0]
        dp[0] = a[0]
        mx = a[0]
        for i in range(1, n):
            dp[i] = a[i] + max(0, dp[i-1])
            mx = max(mx, dp[i])
        
        ans = a[0]
        pref = 0
        for i in range(n-2):
            pref += a[i]
            ans = max(ans, pref+right_max[i+1])
        
        return max(mx, ans)

print(Solution().maxSubarraySumCircular(a=[1,-2,3,-2]))
print(Solution().maxSubarraySumCircular(a=[5,-3,5]))
print(Solution().maxSubarraySumCircular(a=[-3,-2,-3]))