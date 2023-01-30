from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()

        # print(pairs)

        n = len(pairs)
        dp = n * [0]
        dp[0] = 1
        ans = 1
        for i in range(1, n):
            dp[i] = 1
            for j in range(0, i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            ans = max(ans, dp[i])

        # print(dp)

        return ans

print(Solution().findLongestChain(pairs = [[1,2],[2,3],[3,4]]))
print(Solution().findLongestChain(pairs = [[1,2],[7,8],[4,5]]))
print(Solution().findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))