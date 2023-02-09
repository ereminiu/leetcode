from typing import List

class Solution:
    def maximizeWin(self, a: List[int], k: int) -> int:
        n = len(a)
        dp = n * [0]

        ans = 0
        left = 0
        for right in range(n):
            while a[left] < a[right] - k:
                left += 1
            
            dp[right] = max((0 if right == 0 else dp[right-1]), right-left+1)
            ans = max(ans, right - left + 1 + (0 if left == 0 else dp[left-1]))

        return ans 

print(Solution().maximizeWin(a = [1,1,2,2,3,3,5], k = 2))
print(Solution().maximizeWin(a = [1,2,3,4], k = 0))