from typing import List

class Solution:
    def minSwap(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        inf = int(1e9+228)

        dp = [[inf for x in range(2)] for y in range(n)]
        dp[0][0], dp[0][1] = 0, 1

        for i in range(1, n):
            dp[i][0], dp[i][1] = inf, inf
            if a[i] > a[i-1] and b[i] > b[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][0])
                dp[i][1] = min(dp[i][1], dp[i-1][1] + 1)
            if a[i] > b[i-1] and b[i] > a[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][1])
                dp[i][1] = min(dp[i][1], dp[i-1][0]+1)
            # if a[i] > max(a[i-1], b[i-1]) and b[i] > max(a[i-1], b[i-1]):
                # dp[i][1] = min(dp[i][1], dp[i-1][1] + 1)

        # print(*dp, sep='\n')
        
        return min(dp[n-1][0], dp[n-1][1])

print(Solution().minSwap(a=[0,7,8,10,10,11,12,13,19,18], b=[4,4,5,7,11,14,15,16,17,20]))
print(Solution().minSwap(a = [1,3,5,4], b = [1,2,3,7]))
print(Solution().minSwap(a = [0,3,5,8,9], b = [2,1,4,6,9]))
print(Solution().minSwap(a = [2, 2], b = [1, 3]))