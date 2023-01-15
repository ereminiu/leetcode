from typing import List
from collections import Counter

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        memo = Counter()

        def solve(mask):
            if tuple(mask) in memo:
                return memo[tuple(mask)]
            
            ret = 0
            for i in range(n):
                ret += price[i] * mask[i]
                assert mask[i] >= 0
            
            if ret == 0:
                return 0
            
            defaul = mask[::]
            for offer in special:
                relaxed = True
                for i in range(n):
                    if offer[i] > mask[i]:
                        relaxed = False
                        break
                    else:
                        mask[i] -= offer[i]
                
                if relaxed:
                    ret = min(ret, solve(mask) + offer[-1])

                mask = defaul[::]
            
            memo[tuple(mask)] = ret
            return ret
            
        return solve(needs)

print(Solution().shoppingOffers(price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]))
print(Solution().shoppingOffers(price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]))
print(Solution().shoppingOffers(price = [1,1,1], special = [[1,1,0,0],[2,2,1,0]], needs = [1,1,1]))