from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        MOD = int(1e9+7)

        prefix_left, prefix_mul_left = (n+1) * [0], (n+1) * [0]
        prefix_right, prefix_mul_right = (n+1) * [0], (n+1) * [0]

        for i in range(n):
            prefix_left[i+1] = (prefix_left[i] + strength[i]) % MOD
            prefix_mul_left[i+1] = (prefix_mul_left[i] + (i+1) * strength[i]) % MOD
        
        for i in range(n-1, -1, -1):
            prefix_right[i] = (prefix_right[i+1] + strength[i]) % MOD
            prefix_mul_right[i] = (prefix_mul_right[i+1] + (n-i) * strength[i]) % MOD
        
        st = []
        ans = 0
        for i in range(n+1):
            while len(st) and (i == n or strength[st[-1]] >= strength[i]):
                me = st.pop()
                left_idx = 0 if not len(st) else st[-1] + 1
                left_sum = (prefix_mul_left[me + 1] - prefix_mul_left[left_idx] - left_idx * (prefix_left[me + 1] - prefix_left[left_idx])) % MOD
                right_sum = (prefix_mul_right[me + 1] - prefix_mul_right[i] - (n-i) * (prefix_right[me+1] - prefix_right[i])) % MOD
                all = (right_sum * (me - left_idx + 1) + left_sum * (i-me)) % MOD
                ans += all * strength[me]
                ans %= MOD
            
            st.append(i)
        
        return ans

print(Solution().totalStrength(strength = [1,3,1,2]))
print(Solution().totalStrength(strength = [5,4,6]))