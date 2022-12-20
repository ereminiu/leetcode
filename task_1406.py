from typing import List
from functools import cache

class Solution:
    def stoneGameIII(self, value: List[int]) -> str:
        n = len(value)
        right = n * [0]

        right[n-1] = value[n-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + value[i]

        @cache
        def solve(i):
            if i >= n:
                return 0
            return right[i] - min(solve(i+1), solve(i+2), solve(i+3))
        
        alice = solve(0)
        bob = sum(value)-alice
        # print(f'alice = {alice}, bob = {bob}')

        if alice > bob:
            return 'Alice'
        elif alice < bob:
            return 'Bob'
        else:
            return 'Tie'
            

print(Solution().stoneGameIII(value=[1,2,3,7]))
print(Solution().stoneGameIII(value=[1,2,3,-9]))
print(Solution().stoneGameIII(value=[1,2,3,6]))