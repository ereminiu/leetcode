from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        right = n * [0]
        right[n-1] = piles[n-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + piles[i]

        memo = [[-1 for x in range(228)] for y in range(n+1)]
        
        def solve(i, m):
            if i == n:
                memo[i][m] = 0
                return 0
            
            if memo[i][m] != -1:
                return memo[i][m]
            
            profit = 0
            for j in range(i+1, min(n, i+2*m)+1):
                k = max(m, j-i)
                profit = max(profit, right[i] - solve(j, k))
            memo[i][m] = profit
            return profit
        
        return solve(0, 1)

print(Solution().stoneGameII(piles=[2,7,9,4,4]))
print(Solution().stoneGameII(piles=[1,2,3,4,5,100]))