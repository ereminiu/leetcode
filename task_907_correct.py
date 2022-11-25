from typing import List

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        st = []
        dp = n * [0]

        for i in range(n):
            while st and A[st[-1]] > A[i]:
                st.pop()
            if not st:
                dp[i] = (i+1) * A[i]
            else:
                j = st[-1]
                dp[i] = dp[j] + (i-j) * A[i]
            st.append(i)
        
        return sum(dp) % int(1e9+7)

print(Solution().sumSubarrayMins([2, 1, 3, 1]))
print(Solution().sumSubarrayMins([3,1,2,4]))
print(Solution().sumSubarrayMins([11,81,94,43,3]))