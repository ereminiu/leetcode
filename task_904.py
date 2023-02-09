from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        counter = Counter()
        amount = 0
        r = 0
        ans = 1

        for l in range(n-1):
            while r < n and (counter[fruits[r]] != 0 or amount < 2):
                if counter[fruits[r]] == 0:
                    amount += 1
                
                counter[fruits[r]] += 1
                r += 1
            
            ans = max(ans, r-l)

            if counter[fruits[l]] == 1:
                amount -= 1
            
            counter[fruits[l]] -= 1
        
        return ans

print(Solution().totalFruit(fruits = [1,2,1]))
print(Solution().totalFruit(fruits = [0,1,2,2]))
print(Solution().totalFruit(fruits = [1,2,3,2,2]))
print(Solution().totalFruit(fruits = [3,3,3,1,2,1,1,2,3,3,4]))