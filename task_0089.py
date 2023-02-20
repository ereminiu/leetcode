from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:

        def gen(n):
            if n == 1:
                return [0, 1]
            
            prev = gen(n-1)
            ans = prev + prev[::-1]
            for i in range(len(ans) // 2):
                ans[i] = ans[i]
            
            for i in range(len(ans) // 2, len(ans)):
                ans[i] = 2**(n-1) + ans[i]
            
            return ans
        
        return gen(n)

print(Solution().grayCode(n=2))
print(Solution().grayCode(n=1))
print(Solution().grayCode(n=3))