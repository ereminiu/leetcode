from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        st = set()
        
        def go(a, start):
            tpl = tuple(a)
            if len(a) > 1 and tpl not in st:
                ans.append(a[::])
                st.add(tpl)
            
            for i in range(start+1, n):
                if nums[i] >= nums[start]:
                    a.append(nums[i])
                    go(a, i)
                    a.pop()
        
        n = len(nums)
        for i in range(n-1):
            go([nums[i]], i)
        
        return ans

print(Solution().findSubsequences(nums = [4,6,7,7]))
print(Solution().findSubsequences(nums = [4,4,3,2,1]))