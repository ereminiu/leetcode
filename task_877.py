from typing import List
from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        pref = n * [0]
        pref[0] = piles[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + piles[i]

        def get_sum(l, r):
            return pref[r] if l == 0 else pref[r]-pref[l-1]
        
        @cache
        def go(l, r):
            if l == r:
                return piles[l]
            
            return get_sum(l, r) - min(go(l+1, r), go(l, r-1))
        
        alice = go(0, n-1)
        bob = pref[-1] - alice
        # print(f'alice = {alice}, bob = {bob}')
        return alice >= bob

print(Solution().stoneGame(piles=[5,3,4,5]))
print(Solution().stoneGame(piles=[3,7,2,3]))