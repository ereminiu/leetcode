from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        sz = len(strs)
        cnt_zero, cnt_one = sz * [0], sz * [0]
        for i in range(sz):
            cnt_zero[i] = strs[i].count('0')
            cnt_one[i] = strs[i].count('1')
        
        dp = [[0 for x in range(m+1)] for y in range(n+1)]
        
        ans = 0
        for i in range(1, sz+1):
            zeros, ones = strs[i-1].count('0'), strs[i-1].count('1')

            for x in range(n, ones-1, -1):
                for y in range(m, zeros-1, -1):
                    if x == 0 and y == 0:
                        dp[x][y] = 0
                        continue
                    
                    if ones <= x and zeros <= y:
                        dp[x][y] = max(dp[x][y], dp[x-ones][y-zeros] + 1)
                        
                    ans = max(ans, dp[x][y])
                
        return ans

print(Solution().findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))
print(Solution().findMaxForm(strs = ["10","0","1"], m = 1, n = 1))
print(Solution().findMaxForm(strs = ["10","0001","111001","1","0"], m = 1, n = 1))
print(Solution().findMaxForm(strs = ["0001","0101","1000","1000"], m = 9, n = 3))