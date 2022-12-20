from typing import List
from functools import cache

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @cache
        def solve(x):
            if x == 0:
                return False
            
            for y in range(1, int(x**0.5)+1):
                if y**2 <= x and not solve(x-y**2):
                    return True
            
            return False
        
        return solve(n)

print(Solution().winnerSquareGame(n=1))
print(Solution().winnerSquareGame(n=2))
print(Solution().winnerSquareGame(n=4))